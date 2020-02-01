import rhinoscriptsyntax as rs
from Rhino.Input.Custom import *
import scriptcontext
import Rhino
import math

#initialize variables
vector_x = Rhino.Geometry.Vector3d(1,0,0)
vector_y = Rhino.Geometry.Vector3d(0,1,0)
vector_z = Rhino.Geometry.Vector3d(0,1,1)

def FindCentroid(objref):
    objList = Rhino.Collections.TransformObjectList()
    for obj in objref:
        objList.Add(obj)
    return objList.GetBoundingBox(True, False).Center

def PlacePlane(target):
    plane = rs.WorldXYPlane()
    vector = Rhino.Geometry.Vector3d(target)
    plane.Translate(vector)
    return plane

__commandname__ = "ObliquePlan"

def RunCommand( is_interactive ):
    go = GetObject()
    go.SetCommandPrompt("Select objects to be converted to plan oblique")
    go.GetMultiple(1, 0)
    objs = go.Objects() #stores list of objref
    center = FindCentroid(objs)
    plane = PlacePlane(center)
    
    for obj in objs:
        xform_shear = Rhino.Geometry.Transform.Shear(plane, vector_x, vector_y, vector_z)
        xform_rotation = Rhino.Geometry.Transform.Rotation(45 * math.pi / 180, center)
        scriptcontext.doc.Objects.Transform(obj, xform_shear * xform_rotation, True)
        rs.ObjectName(objs, "Oblique Plan")

    return 0

#RunCommand(True)
