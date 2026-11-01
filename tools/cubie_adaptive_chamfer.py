"""Safely apply physical C0.5 chamfers to approved source; reject local cuts that corrupt serialized geometry."""
import numpy as np,trimesh,time
from manifold3d import Manifold,Mesh,OpType
import runpy
source=runpy.run_path('tools/cubie_rebuild_front.py')
M=source['out']
assert M.is_watertight and M.is_winding_consistent and len(M.split(only_watertight=False))==1
v=M.vertices;f=M.faces;e=M.face_adjacency_edges;p=M.face_adjacency
angs=np.rad2deg(M.face_adjacency_angles);lens=np.linalg.norm(v[e[:,1]]-v[e[:,0]],axis=1)
norm=M.face_normals
f2=f[p[:,1]]
other=np.where((f2!=e[:,0,None])&(f2!=e[:,1,None]),f2,-1).max(axis=1)
mid=v[e].mean(1)
convex=np.einsum('ij,ij->i',norm[p[:,0]],v[other]-mid)<-1e-5
C=np.array([87.5,54,-1.4779667096744553])
th=np.deg2rad(16);rel=mid-C
yl=np.cos(th)*rel[:,1]+np.sin(th)*rel[:,2]
zl=-np.sin(th)*rel[:,1]+np.cos(th)*rel[:,2]
rr=np.hypot(rel[:,0],yl)
protect=(rr<37)&(rr>32)&(zl>-15)&(zl<15)
chosen=np.where((angs>80)&(angs<100)&(lens>=.5)&convex&~protect)[0]
assert 500<len(chosen)<3000
def manifold(mesh):
 return Manifold(Mesh(vert_properties=np.ascontiguousarray(mesh.vertices,dtype=np.float32),tri_verts=np.ascontiguousarray(mesh.faces,dtype=np.uint32)))
cutters=[]
for ii in chosen:
 a,b=e[ii];n1,n2=norm[p[ii]];dot=np.dot(n1,n2)
 if abs(dot)>.99:continue
 u1=-(n2-dot*n1)/np.sqrt(1-dot*dot)
 u2=-(n1-dot*n2)/np.sqrt(1-dot*dot)
 outward=(n1+n2)/np.linalg.norm(n1+n2)
 q=np.array([v[a]+.03*outward,v[a]+.5*u1,v[a]+.5*u2,
             v[b]+.03*outward,v[b]+.5*u1,v[b]+.5*u2])
 face=np.array([(0,2,1),(3,4,5),(0,1,4),(0,4,3),(1,2,5),(1,5,4),(2,0,3),(2,3,5)])
 block=trimesh.Trimesh(vertices=q,faces=face,process=False)
 if block.volume<0:block.invert()
 assert block.is_watertight and block.volume>0
 cutters.append((ii,manifold(block)))
print('ADAPTIVE CANDIDATES',len(cutters),flush=True)
# Local vertex rounding and duplicate-shell checks are mandatory. Manifold
# "watertight=True" BEFORE STL serialization alone is insufficient.
def valid(solid):
 m=solid.to_mesh()
 geo=trimesh.Trimesh(vertices=np.array(m.vert_properties)[:,:3],
                    faces=np.array(m.tri_verts),process=True)
 if not (geo.is_watertight and geo.is_winding_consistent):return False,'open-or-overlapping'
 if len(geo.split(only_watertight=False))!=1:return False,'separate-shells'
 if min(trimesh.triangles.area(geo.triangles))<1e-10:return False,'collapsed-triangles'
 return True,'ok'
original=source['result']
print('INITIAL VALIDITY',valid(original),flush=True)
assert valid(original)[0]
# Group geometrically nearby edges to avoid arbitrary nondeterministic fit.
cutters.sort(key=lambda t:(int(mid[t[0],0]/12),int(mid[t[0],1]/12),int(mid[t[0],2]/12),float(mid[t[0],0]),float(mid[t[0],1])))
accepted=[];rejected=[];calls=0
t0=time.monotonic()
def apply(current,groups):
 global calls
 calls+=1
 try:
  shapes=[x[1] for x in groups]
  tool=shapes[0] if len(shapes)==1 else Manifold.batch_boolean(shapes,OpType.Add)
  proposed=current-tool
  loss=current.volume()-proposed.volume()
  ok,reason=valid(proposed) if loss>1e-6 else (False,'no-material-cut')
  if ok:
   accepted.extend(z[0] for z in groups)
   return proposed
 except Exception as ex:
  reason=type(ex).__name__
 if len(groups)==1:
  rejected.append((groups[0][0],reason))
  return current
 half=len(groups)//2
 current=apply(current,groups[:half])
 return apply(current,groups[half:])
current=original
for i in range(0,len(cutters),60):
 current=apply(current,cutters[i:i+60])
 if i%180==0:print('PROGRESS',i,'accepted',len(accepted),'rejected',len(rejected),'sec',round(time.monotonic()-t0,1),flush=True)
assert valid(current)[0]
print('ADAPTIVE DONE accepted',len(accepted),'rejected',len(rejected),'calls',calls,'sec',round(time.monotonic()-t0,2),flush=True)
print('ADAPTIVE REMOVED',original.volume()-current.volume(),flush=True)
out=current.to_mesh()
mesh=trimesh.Trimesh(vertices=np.array(out.vert_properties)[:,:3],faces=np.array(out.tri_verts),process=True)
assert mesh.is_watertight and len(mesh.split(only_watertight=False))==1
mesh.export('cubie_adaptive_valid_chamfer.stl')
np.savez_compressed('cubie_chamfer_accept_reject.npz',accepted=np.array(accepted,dtype=int),rejected=np.array([q[0] for q in rejected],dtype=int))
