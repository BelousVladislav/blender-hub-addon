import bpy
import requests
from bpy.types import Operator, Panel, PropertyGroup
from bpy.utils import register_class, unregister_class
from bpy.props import BoolProperty, PointerProperty, StringProperty

class SendToFreeRenderProps(PropertyGroup):
    projectId: StringProperty(
        name = "ProjectId",
        description = "Use the ProjectId from your freerender project"
#        subtype = "PASSWORD"
    )
    token: StringProperty(
        name = "UUID Project Token",
        description = "Use the token from your freerender account",
        subtype = "PASSWORD"
    )
    isPublish: BoolProperty(
        name = 'Publish on FreeBlender',
        default = True
    )

class SendToFreeRender(Operator):
    bl_idname = 'render.send_freerender'
    bl_label = 'Send To FreeBlender'
    
    def execute(self, context) -> set:
        projectId = context.object.rend.projectId
        token = context.object.rend.token
        test_file = open(bpy.data.filepath, "rb")
        r = requests.post("http://213.231.7.96:9000/api/project/uploadFileFromBlender/"+projectId+"/"+token, files = {"file": test_file})
        print(r)
        print("YEEEEEAAAAAA")
#        raise NotImplementedError
        return {'FINISHED'}
    
class OBJECT_PT_SendToFreeRenderPanel(Panel):
    bl_label = "Render with FreeBlender"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = 'Render'
    
    def draw(self, context):
        layout = self.layout
        props = context.object.rend
        col = layout.column()
        col.prop(props, "projectId")
        col.prop(props, "token")
        col.column()
        col.prop(props, "isPublish")
        row = layout.row()
        row.operator("render.send_freerender")
        
        

classes = [
    SendToFreeRenderProps,
    SendToFreeRender,
    OBJECT_PT_SendToFreeRenderPanel,
]

def register():
    for cl in classes:
        register_class(cl)
    bpy.types.Object.rend = PointerProperty(type = SendToFreeRenderProps)
        
def unregister():
    for cl in reversed(classes):
        unregister_class(cl)
        
if __name__ == '__main__':
    register()
#    bpy.ops.render.send_freerender()





#print(bpy.data.filepath)
#test_file = open(bpy.data.filepath, "rb")
#r = requests.post("http://192.168.31.232:3000/uploadFile", files = {"file": test_file})
#print(r)