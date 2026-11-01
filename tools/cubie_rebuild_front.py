import base64,json,hashlib
from pathlib import Path
import numpy as np,trimesh
from manifold3d import Manifold,Mesh
BASE=Path('Kohutavalt kaua ver.1.html')
SHA='661666f196459ec15edce3b1fe39cd552ce4a25dd7212a606bf7cf77d3bdbe91'
raw=BASE.read_bytes()
assert len(raw)==5527796 and hashlib.sha256(raw).hexdigest()==SHA
s=raw.decode('utf8');p=s.index('const geometry=')+len('const geometry=')
geo,_=json.JSONDecoder().raw_decode(s[p:])
assert len(geo)==12 and geo[0]['triangles']==71880
q=np.frombuffer(base64.b64decode(geo[0]['q']),dtype='<f4').reshape(-1,3)
src=trimesh.Trimesh(vertices=q,faces=np.arange(len(q)).reshape(-1,3),process=True,validate=False)
assert len(src.vertices)==35932 and src.is_watertight and src.is_winding_consistent
v=src.vertices.astype(np.float32).copy()
v[17043]+=np.array([0.,-.9612618,-.2756371],np.float32)*.001
assert trimesh.Trimesh(vertices=v,faces=src.faces,process=False).is_watertight
def manifold(mesh):
 return Manifold(Mesh(vert_properties=np.ascontiguousarray(mesh.vertices,dtype=np.float32),tri_verts=np.ascontiguousarray(mesh.faces,dtype=np.uint32)))
solid=manifold(trimesh.Trimesh(vertices=v,faces=src.faces,process=False))
assert solid.num_tri()>70000 and abs(solid.volume()-src.volume)<.01
print('ORIGINAL',solid.num_tri(),solid.volume(),flush=True)
C=np.array([87.5,54,-1.4779667096744553],float)
a=np.deg2rad(16)
X=np.array([1.,0,0]);Y=np.array([0,np.cos(a),np.sin(a)]);Z=np.cross(X,Y)
n=320;tt=np.linspace(0,np.pi,n+1)
r0,r1=35.500025,36.5
z0,z1=-40.,0.
vt=np.array([C+z*Z+r*np.cos(t)*X+r*np.sin(t)*Y for z in (z0,z1) for r in (r0,r1) for t in tt],float)
def ix(zi,ri,i):return (zi*2+ri)*(n+1)+i
ff=[]
for ri in range(2):
 for i in range(n):
  p0,p1,p2,p3=ix(0,ri,i),ix(0,ri,i+1),ix(1,ri,i+1),ix(1,ri,i)
  if ri:ff.extend([(p0,p1,p2),(p0,p2,p3)])
  else:ff.extend([(p0,p2,p1),(p0,p3,p2)])
for zi in range(2):
 for i in range(n):
  p0,p1,p2,p3=ix(zi,0,i),ix(zi,1,i),ix(zi,1,i+1),ix(zi,0,i+1)
  if zi:ff.extend([(p0,p1,p2),(p0,p2,p3)])
  else:ff.extend([(p0,p2,p1),(p0,p3,p2)])
for i in (0,n):
 p0,p1,p2,p3=ix(0,0,i),ix(0,1,i),ix(1,1,i),ix(1,0,i)
 if i==n:ff.extend([(p0,p2,p1),(p0,p3,p2)])
 else:ff.extend([(p0,p1,p2),(p0,p2,p3)])
tool=trimesh.Trimesh(vertices=vt,faces=np.array(ff,dtype=int),process=False)
if tool.volume<0:tool.invert()
assert tool.is_watertight and tool.is_winding_consistent and tool.volume>0
cut=manifold(tool)
assert cut.status().name=='NoError'
result=solid-cut
assert result.num_tri()>70000 and 0<result.volume()<solid.volume()
me=result.to_mesh()
out=trimesh.Trimesh(vertices=np.array(me.vert_properties)[:,:3],faces=np.array(me.tri_verts),process=False)
assert out.is_watertight and out.is_winding_consistent and out.volume>0
print('WS FRONT CUT',len(out.faces),out.volume,'removed',solid.volume()-result.volume(),flush=True)
# Structural XLR opening probe, never guess XLR movement.
cyl=trimesh.creation.cylinder(radius=11.9,height=30.0,sections=320)
cyl.apply_translation([125.6,24.9,14.9])
probe=solid-manifold(cyl)
print('XLR BORE PROBE SOLID REMOVAL',solid.volume()-probe.volume(),flush=True)
for radius in (11.5,11.8,11.88):
 cylinder=trimesh.creation.cylinder(radius=radius,height=27.2,sections=320)
 cylinder.apply_translation([125.6,24.9,13.75])
 delta=solid.volume()-(solid-manifold(cylinder)).volume()
 print('XLR INTERIOR',radius,'mm, removed',delta,'mm3',flush=True)
out.export('cubie_fresh_ws73_front.stl')
assert hashlib.sha256(BASE.read_bytes()).hexdigest()==SHA
