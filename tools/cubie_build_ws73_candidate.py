from pathlib import Path
import json, base64, hashlib, re, subprocess, shutil, sys
import numpy as np
import trimesh

source=Path("Kohutavalt kaua ver.1.html")
original=source.read_bytes()
baseline_hash="661666f196459ec15edce3b1fe39cd552ce4a25dd7212a606bf7cf77d3bdbe91"
assert len(original)==5527796 and hashlib.sha256(original).hexdigest()==baseline_hash
mesh=trimesh.load(sys.argv[1],process=True)
assert mesh.is_watertight and mesh.is_winding_consistent and len(mesh.faces)==74274
s=original.decode("utf8")
p=s.index("const geometry=")+len("const geometry=")
items,n=json.JSONDecoder().raw_decode(s[p:])
assert len(items)==12 and items[0]["triangles"]==71880 and items[0]["encoding"]=="float32-mm"
triangle_data=np.ascontiguousarray(mesh.vertices[mesh.faces].reshape(-1),dtype="<f4")
items[0]["q"]=base64.b64encode(triangle_data.tobytes()).decode("ascii")
items[0]["triangles"]=len(mesh.faces)
items[0].pop("flat",None)
s=s[:p]+json.dumps(items,ensure_ascii=False,separators=(",",":"))+s[p+n:]
patches=[
 ("const initiallyVisible=true;","const initiallyVisible=entry.name.startsWith('Konstruktsioon');"),
 ("document.getElementById('reset').onclick=()=>{orthographic=true;az=0;el=0;distance=fit;panX=0;panY=0;draw();};","document.getElementById('reset').onclick=()=>{orthographic=true;az=0;el=0;distance=fit;panX=0;panY=0;for(const g of groups)g.visible=g.isPanel;for(const row of document.querySelectorAll('#items .item')){const g=groups[Number(row.dataset.index)];row.classList.toggle('off',!g.visible);}draw();};"),
 ("1 mm võrk · eraldi osad (klõps peidab)","1 mm võrk · eraldi osad (klõps näitab/peidab)")
]
for a,b in patches:
 assert s.count(a)==1,a
 s=s.replace(a,b)
candidate=Path("Cubie_A7A_v02_WS73_tookandidaat.html")
assert not candidate.exists()
candidate.write_text(s,encoding="utf8")
digest=hashlib.sha256(candidate.read_bytes()).hexdigest()
assert digest=="c96ec534c9019d8845475e5c8884d75010e62794937973190fbe148c4b8be6c1"
for i,script in enumerate(re.findall(r"<script(?:\s[^>]*)?>(.*?)</script>",s,re.S|re.I)):
 f=Path("/tmp/cubie_script_%d.js"%i)
 f.write_text(script)
 subprocess.run(["node","--check",str(f)],check=True)
site=Path("_site")
site.mkdir(exist_ok=False)
shutil.copyfile(candidate,site/"index.html")
shutil.copyfile(candidate,site/"v02.html")
assert hashlib.sha256(source.read_bytes()).hexdigest()==baseline_hash
print("VERIFIED SHA256",digest)
print("NOTICE: v02 is a working candidate containing WS73 only. XLR/C0.5 work remains.",flush=True)
