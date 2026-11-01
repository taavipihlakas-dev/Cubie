from pathlib import Path
import numpy as np, trimesh, manifold3d
from scipy.spatial import cKDTree
from manifold3d import Manifold, Mesh

src=Path("/tmp/cubie_xlr/waveshare_73_simplified_probe.stl")
assert src.is_file()
base=trimesh.load(src,process=True)
assert base.is_watertight and base.is_winding_consistent and base.volume>0
print("XLR_INPUT",len(base.faces),base.volume,flush=True)

def asman(mesh):
    return Manifold(Mesh(vert_properties=np.ascontiguousarray(mesh.vertices,dtype=np.float32),
                         tri_verts=np.ascontiguousarray(mesh.faces,dtype=np.uint32)))
def cyl(x,y,r,zmin,zmax,n=256):
    m=trimesh.creation.cylinder(radius=r,height=zmax-zmin,sections=n)
    m.apply_translation([x,y,(zmin+zmax)/2])
    assert m.is_watertight and m.is_winding_consistent
    return asman(m)

X,Y=125.6,24.9
dx,dy=0.4,-0.5
old=asman(base)
print("XLR_MANIFOLD_IN",old.status(),old.num_tri(),flush=True)
# Close old Ø23.8-mm bore only in the 0..28 mm front/back aperture,
# cutting its replacement with matching cylindrical radius.
fill=cyl(X,Y,12.02,-0.01,28.1)
# Precisely preserve the existing small front lip: inner bore Ø23.8 until
# z27.5, then a half-millimeter radial taper to Ø22.8 at the front face.
def bore_with_front_lip(cx,cy,n=256):
    angles=np.linspace(0,2*np.pi,n,endpoint=False)
    rings=[(-.02,11.9),(27.5,11.9),(28.0,11.4),(28.12,11.4)]
    vertices=np.array([[cx+r*np.cos(t),cy+r*np.sin(t),z]
        for z,r in rings for t in angles],dtype=np.float64)
    vertices=np.vstack([vertices,[cx,cy,rings[0][0]],[cx,cy,rings[-1][0]]])
    faces=[]
    for j in range(len(rings)-1):
        for k in range(n):
            kk=(k+1)%n
            a,b,c,d=j*n+k,j*n+kk,(j+1)*n+kk,(j+1)*n+k
            faces.extend([(a,b,c),(a,c,d)])
    bottom=len(vertices)-2
    top=len(vertices)-1
    for k in range(n):
        kk=(k+1)%n
        faces.append((bottom,kk,k))
        faces.append((top,(len(rings)-1)*n+k,(len(rings)-1)*n+kk))
    mesh=trimesh.Trimesh(vertices=vertices,faces=faces,process=False)
    if mesh.volume<0:mesh.invert()
    assert mesh.is_watertight and mesh.is_winding_consistent
    return asman(mesh)
newbore=bore_with_front_lip(X+dx,Y+dy)
with_fill=old+fill
print("XLR_AFTER_FILL",with_fill.status(),with_fill.num_tri(),with_fill.volume(),flush=True)
fixed=with_fill-newbore
print("XLR_AFTER_SHIFT",fixed.status(),fixed.num_tri(),fixed.volume(),flush=True)
assert fixed.num_tri()>5000 and fixed.volume()>0
m=fixed.to_mesh()
out=trimesh.Trimesh(vertices=np.asarray(m.vert_properties)[:,:3],faces=np.asarray(m.tri_verts),process=False)
print("XLR_MESH",out.is_watertight,out.is_winding_consistent,len(out.faces),out.volume,flush=True)
assert out.is_watertight and out.is_winding_consistent
assert abs(out.volume-base.volume)<500
# These measured checks do not alone prove absence of ring-vs-hole intersection.
out.export("/tmp/cubie_xlr/xlr_shift_probe.stl")
print("XLR_PROBE_EXPORTED",flush=True)
