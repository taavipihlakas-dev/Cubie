"""Rebuild an OpenCascade CAD BREP from ONLY the approved Cubie HTML.

This yields a valid faceted CAD solid, not a feature-history/parametric design.
Source HTML is read-only. Requires numpy, trimesh, cadquery-ocp.
"""
import base64,hashlib,json,sys
from pathlib import Path
import numpy as np,trimesh
from OCP.BRep import BRep_Builder
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeVertex,BRepBuilderAPI_MakeEdge,BRepBuilderAPI_MakeWire,BRepBuilderAPI_MakeFace,BRepBuilderAPI_MakeSolid
from OCP.BRepCheck import BRepCheck_Analyzer
from OCP.BRepTools import BRepTools
from OCP.TopoDS import TopoDS,TopoDS_Shell
from OCP.gp import gp_Pnt
from OCP.BRepGProp import BRepGProp
from OCP.GProp import GProp_GProps

SHA="661666f196459ec15edce3b1fe39cd552ce4a25dd7212a606bf7cf77d3bdbe91"

def convert(original="Kohutavalt kaua ver.1.html",dest="Cubie_A7A_CAD_tooalus.brep"):
    f=Path(original);src=f.read_bytes()
    assert hashlib.sha256(src).hexdigest()==SHA and len(src)==5527796
    s=src.decode("utf8");p=s.index("const geometry=")+len("const geometry=")
    objects,_=json.JSONDecoder().raw_decode(s[p:])
    assert len(objects)==12 and objects[0]["triangles"]==71880
    assert objects[0]["encoding"]=="float32-mm"
    soup=np.frombuffer(base64.b64decode(objects[0]["q"]),dtype="<f4").reshape(-1,3)
    mesh=trimesh.Trimesh(vertices=soup,faces=np.arange(len(soup)).reshape(-1,3),process=True,validate=False)
    assert len(mesh.vertices)==35932 and len(mesh.faces)==71880
    assert mesh.is_watertight and mesh.is_winding_consistent
    verts=mesh.vertices.copy();faces=mesh.faces
    assert (trimesh.triangles.area(verts[faces])==0).sum()==1
    # One collapsed triangle; move ONE vertex 0.001 mm, in working copy only.
    verts[17043]+=np.array([0,-.9612618,-.2756371])*.001
    repair=trimesh.Trimesh(vertices=verts,faces=faces,process=False)
    assert repair.is_watertight and repair.is_winding_consistent
    assert (trimesh.triangles.area(verts[faces])==0).sum()==0
    assert abs(repair.volume-mesh.volume)<.01
    bb=BRep_Builder();shell=TopoDS_Shell();bb.MakeShell(shell)
    vv={};ee={}
    for n,face in enumerate(faces):
        oriented=[]
        for j in range(3):
            a,b=int(face[j]),int(face[(j+1)%3]);key=tuple(sorted((a,b)))
            if key not in ee:
                for i in key:
                    if i not in vv:vv[i]=BRepBuilderAPI_MakeVertex(gp_Pnt(*map(float,verts[i]))).Vertex()
                ee[key]=BRepBuilderAPI_MakeEdge(vv[key[0]],vv[key[1]]).Edge()
            e=ee[key]
            oriented.append(e if a==key[0] else TopoDS.Edge_s(e.Reversed()))
        w=BRepBuilderAPI_MakeWire()
        for e in oriented:w.Add(e)
        assert w.IsDone(),n
        face_obj=BRepBuilderAPI_MakeFace(w.Wire(),True)
        assert face_obj.IsDone(),n
        bb.Add(shell,face_obj.Face())
        if (n+1)%20000==0:print("CAD faces",n+1,flush=True)
    solid=BRepBuilderAPI_MakeSolid(shell).Solid()
    assert BRepCheck_Analyzer(solid).IsValid()
    g=GProp_GProps();BRepGProp.VolumeProperties_s(solid,g)
    assert abs(g.Mass()-mesh.volume)<.01
    BRepTools.Write_s(solid,dest)
    assert Path(dest).stat().st_size>1_000_000
    assert hashlib.sha256(f.read_bytes()).hexdigest()==SHA
    print("VALID FACETED CAD BREP",dest,"volume_mm3",g.Mass(),flush=True)

if __name__=="__main__":convert(*(sys.argv[1:]))
