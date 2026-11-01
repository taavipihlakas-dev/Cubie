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
dx,dy=0.5,-1.2
old=asman(base)
print("XLR_MANIFOLD_IN",old.status(),old.num_tri(),flush=True)
# Close old Ø23.8-mm bore only in the 0..28 mm front/back aperture,
# cutting its replacement with matching cylindrical radius.
fill=cyl(X,Y,12.02,-0.01,28.1)
newbore=cyl(X+dx,Y+dy,11.9,-.02,28.12)
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
