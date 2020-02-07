import rhinoscriptsyntax as rs
import random

__commandname__ = "RandomRotate"

def RunCommand( is_interactive ):
    objs = rs.GetObjects("Select objects to rotate")
    
    if objs:
        for obj in objs:
            point = rs.SurfaceAreaCentroid(obj)[0]
            rs.RotateObject(obj, point, random.random() * 360, None, copy=False)
    return 0

#RunCommand(True)