bl_info = {
    "name": "UV Rotate and Rename",
    "blender": (2, 80, 0),
    "category": "UV",
}

import bpy
import bmesh
from math import radians

class UVRotateRenameOperator(bpy.types.Operator):
    """Copy the first UV map, rename it to 'UVMap', and rotate it by 90 degrees on the Z axis for multiple selected meshes"""
    bl_idname = "uv.uv_rotate_rename"
    bl_label = "Rotate and Rename UV Map"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        selected_objects = context.selected_objects
        processed_objects = 0

        for obj in selected_objects:
            if obj.type != 'MESH':
                continue

            mesh = obj.data
            if not mesh.uv_layers:
                self.report({'WARNING'}, f"No UV maps found on object {obj.name}")
                continue

            # Copy the first UV map
            uv_layer = mesh.uv_layers[0]
            new_uv_layer = mesh.uv_layers.new(name="UVMap")

            for loop in mesh.loops:
                new_uv_layer.data[loop.index].uv = uv_layer.data[loop.index].uv

            # Rotate the new UV map by 90 degrees on the Z axis
            bm = bmesh.new()
            bm.from_mesh(mesh)
            uv_layer = bm.loops.layers.uv[new_uv_layer.name]

            for face in bm.faces:
                for loop in face.loops:
                    uv = loop[uv_layer].uv
                    uv.x, uv.y = -uv.y, uv.x  # Rotate 90 degrees

            bm.to_mesh(mesh)
            bm.free()
            
            processed_objects += 1

        self.report({'INFO'}, f"Processed {processed_objects} object(s)")
        return {'FINISHED'}

class UV_PT_RotateRenamePanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "UV Rotate and Rename"
    bl_idname = "UV_PT_rotate_rename"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'UV Rotate'

    def draw(self, context):
        layout = self.layout
        layout.operator(UVRotateRenameOperator.bl_idname)

def menu_func(self, context):
    self.layout.operator(UVRotateRenameOperator.bl_idname)

def register():
    bpy.utils.register_class(UVRotateRenameOperator)
    bpy.utils.register_class(UV_PT_RotateRenamePanel)
    bpy.types.VIEW3D_MT_uv_map.append(menu_func)

def unregister():
    bpy.utils.unregister_class(UVRotateRenameOperator)
    bpy.utils.unregister_class(UV_PT_RotateRenamePanel)
    bpy.types.VIEW3D_MT_uv_map.remove(menu_func)

if __name__ == "__main__":
    register()
