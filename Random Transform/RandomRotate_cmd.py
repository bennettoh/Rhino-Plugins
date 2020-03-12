from Rhino.Input.Custom import *
import rhinoscriptsyntax as rs
import random

__commandname__ = "RandomRotate"

def RunCommand( is_interactive ):
    go = GetObject()
    go.SetCommandPrompt("Select objects to rotate randomly")
    go.GetMultiple(1, 0)
    objs = go.Objects() #stores objref
    
    if objs:
        for obj in objs:
            object = obj.Object()
            if(str(object.ObjectType) == "InstanceReference"):
                print "issa block"
#                point = rs.SurfaceAreaCentroid(obj.Geometry.Id)[0]
                point = rs.BlockInstanceInsertPoint(obj)
                rs.RotateObject(obj, point, random.random() * 360, None, copy=False)
            else:
                print "issa obj"
                rotateObj(obj)
    return 0

#def rotateBlock(obj):
#    block_id = obj
#    block_name = rs.BlockInstanceName(block_id)
#    block_base_point = rs.BlockInstanceInsertPoint(block_id)
#    objects_ids = rs.ExplodeBlockInstance(block_id)
#    rotateObj(objects_ids)
#    rs.SelectObjects(objects_ids)
#    rs.InsertBlock(block_name, block_base_point)
#    rs.DeleteObjects(objects_ids)

def rotateObj(obj):
    point = rs.SurfaceAreaCentroid(obj)[0]
    rs.RotateObject(obj, point, random.random() * 360, None, copy=False)

#RunCommand(True)