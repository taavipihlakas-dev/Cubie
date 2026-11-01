import numpy as np,trimesh
from manifold3d import Manifold,Mesh,OpType
from pathlib import Path
root='/tmp/cubie_chamfer'
M=trimesh.load(root+'/cubie_fresh_ws73_front.stl',process=True)
assert M.is_watertight and M.is_winding_consistent
v=M.vertices;f=M.faces
edges=M.face_adjacency_edges;pair=M.face_adjacency
angles=np.rad2deg(M.face_adjacency_angles);lengths=np.linalg.norm(v[edges[:,1]]-v[edges[:,0]],axis=1)
norm=M.face_normals
f2=f[pair[:,1]]
other=np.where((f2!=edges[:,0,None])&(f2!=edges[:,1,None]),f2,-1).max(axis=1)
mid=(v[edges[:,0]]+v[edges[:,1]])/2
convex=np.einsum('ij,ij->i',norm[pair[:,0]],v[other]-mid)>1e-5
# Diagnostic controlled subset: long straight structural edges. Exclude the ring region.
r=np.hypot(mid[:,0]-87.5,mid[:,1]-54)
# Detect all eligible high-angle, edge-length >=0.5 structural corners;
# preserve the Ø71 ring and its adjacent unmodified lower arc.
C=np.array([87.5,54,-1.4779667096744553])
tilt=np.deg2rad(16)
relative=mid-C
ylocal=np.cos(tilt)*relative[:,1]+np.sin(tilt)*relative[:,2]
zlocal=-np.sin(tilt)*relative[:,1]+np.cos(tilt)*relative[:,2]
rlocal=np.hypot(relative[:,0],ylocal)
protected=(rlocal<37)&(rlocal>32)&(zlocal>-15)&(zlocal<15)
chosen=np.where((angles>80)&(angles<100)&(lengths>=2)&convex&~protected)[0]
print('CHAMFER CANDIDATE COUNT',len(chosen),flush=True)
assert 5<len(chosen)<200
def mm(mesh):
 return Manifold(Mesh(vert_properties=np.ascontiguousarray(mesh.vertices,dtype=np.float32),tri_verts=np.ascontiguousarray(mesh.faces,dtype=np.uint32)))
cutters=[]
for index in chosen:
 a,b=edges[index];n1,n2=norm[pair[index]]
 dot=np.dot(n1,n2)
 if abs(dot)>.99:continue
 u1=(n2-dot*n1)/np.sqrt(1-dot*dot)
 u2=(n1-dot*n2)/np.sqrt(1-dot*dot)
 out=(n1+n2)/np.linalg.norm(n1+n2)
 p0=v[a]-out*.03
 p3=v[b]-out*.03
 p1=v[a]+u1*.5;p2=v[a]+u2*.5
 p4=v[b]+u1*.5;p5=v[b]+u2*.5
 verts=np.array([p0,p1,p2,p3,p4,p5])
 faces=np.array([(0,2,1),(3,4,5),(0,1,4),(0,4,3),(1,2,5),(1,5,4),(2,0,3),(2,3,5)])
 prism=trimesh.Trimesh(vertices=verts,faces=faces,process=False)
 if prism.volume<0:prism.invert()
 assert prism.is_watertight and prism.is_winding_consistent and prism.volume>0
 piece=mm(prism)
 assert piece.status().name=='NoError'
 cutters.append(piece)
print('CUTTERS',len(cutters),flush=True)
union=Manifold.batch_boolean(cutters,OpType.Add)
print('UNION',union.status(),union.num_tri(),union.volume(),flush=True)
old=mm(M)
new=old+union
print('AFTER CHAMFER',new.status(),new.num_tri(),new.volume(),'REMOVED',new.volume()-old.volume(),flush=True)
assert new.num_tri()>len(M.faces)*0.8 and new.volume()>0
outmesh=new.to_mesh()
out=trimesh.Trimesh(vertices=np.asarray(outmesh.vert_properties)[:,:3],faces=np.asarray(outmesh.tri_verts),process=False)
print('WATERTIGHT',out.is_watertight,'WINDING',out.is_winding_consistent,flush=True)
assert out.is_watertight and out.is_winding_consistent and (new.volume()-old.volume())>0.05
out.export('cubie_concave_structural_probe.stl')
