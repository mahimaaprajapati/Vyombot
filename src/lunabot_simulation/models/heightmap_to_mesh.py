import bpy
import os

# --- CLEAN DEFAULT SCENE ---
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# --- IMAGE PATH ---
img_path = "/home/mahimaa/Vyombot/ros2_ws/src/lunabot_simulation/models/moon_heightmap_sq.png"

# --- CREATE PLANE ---
bpy.ops.mesh.primitive_plane_add(size=50, location=(0,0,0))
obj = bpy.context.active_object

# --- SUBDIVIDE ---
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.subdivide(number_cuts=200)
bpy.ops.object.mode_set(mode='OBJECT')

# --- DISPLACEMENT TEXTURE ---
tex = bpy.data.textures.new("disp_tex", type='IMAGE')
tex.image = bpy.data.images.load(img_path)

disp = obj.modifiers.new(name="Displace", type='DISPLACE')
disp.texture = tex
disp.strength = 10

# --- APPLY MODIFIER ---
bpy.ops.object.modifier_apply(modifier="Displace")

# --- EXPORT OBJ ---
out = "/home/mahimaa/Vyombot/ros2_ws/src/lunabot_simulation/models/moon.obj"
bpy.ops.export_scene.obj(filepath=out)

print("=== TERRAIN EXPORTED TO OBJ ===")
