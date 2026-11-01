import bpy, bmesh, math, sys
from pathlib import Path

SOURCE = "/tmp/cubie_bevel/waveshare_73_simplified_probe.stl"
OUTPUT = "/tmp/cubie_bevel/waveshare_73_beveled_probe.stl"
assert Path(SOURCE).is_file()
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)
try:
    bpy.ops.wm.stl_import(filepath=SOURCE)
except Exception:
    import addon_utils
    addon_utils.enable("io_mesh_stl", default_set=False)
    bpy.ops.import_mesh.stl(filepath=SOURCE)
obj=bpy.context.view_layer.objects.active
assert obj is not None
bm=bmesh.new()
bm.from_mesh(obj.data)
bmesh.ops.remove_doubles(bm,verts=list(bm.verts),dist=1e-5)
bm.verts.ensure_lookup_table()
bm.edges.ensure_lookup_table()
sharp=[e for e in bm.edges if e.is_manifold and e.calc_face_angle(0)>math.radians(70)]
short=[e for e in sharp if e.calc_length()<1]
print("BEVEL_INPUT",len(bm.verts),len(bm.faces),"sharp",len(sharp),"under1mm",len(short),flush=True)
assert len(sharp)>200
result=bmesh.ops.bevel(bm,geom=sharp,offset=.5,offset_type="OFFSET",segments=1,
                       profile=0.5,affect="EDGES",clamp_overlap=True,
                       loop_slide=True,miter_outer="SHARP",miter_inner="SHARP")
print("BEVEL_RESULT",len(result["faces"]),len(bm.faces),len(bm.verts),flush=True)
boundary=[e for e in bm.edges if not e.is_manifold]
print("BEVEL_EDGES_NOT_MANIFOLD",len(boundary),flush=True)
assert not boundary
bmesh.ops.triangulate(bm,faces=list(bm.faces),quad_method='BEAUTY',ngon_method='BEAUTY')
bmesh.ops.remove_doubles(bm,verts=list(bm.verts),dist=1e-5)
print("AFTER_TRIANGULATE",len(bm.faces),len([e for e in bm.edges if not e.is_manifold]),flush=True)
assert all(e.is_manifold for e in bm.edges)
bm.to_mesh(obj.data)
bm.free()
obj.data.update()
try:
    bpy.ops.wm.stl_export(filepath=OUTPUT,export_selected_objects=False,ascii_format=False)
except Exception:
    bpy.ops.export_mesh.stl(filepath=OUTPUT,use_selection=False,ascii=False)
print("BEVEL_OUTPUT",Path(OUTPUT).stat().st_size,flush=True)
