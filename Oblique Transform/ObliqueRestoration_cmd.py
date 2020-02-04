import rhinoscriptsyntax as rs
import Rhino
import scriptcontext
import System.Guid
import Rhino.DocObjects
import math


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

def FindObjectsByName(name):
    settings = Rhino.DocObjects.ObjectEnumeratorSettings()
    settings.NameFilter = name
    objects = scriptcontext.doc.Objects.GetObjectList(settings) #returns a IEnumerable<RhinoObject>
    
    if not objects:
        return 0
    
    obj_ref = [] #Convert to list of ObjRef objects
    for object in objects:
        obj_ref.append(Rhino.DocObjects.ObjRef(object))
    
    return obj_ref

def CustomTransformation(objs, vector_x, vector_y, vector_z, angle, message):
    center = FindCentroid(objs)
    plane = PlacePlane(center)
    
    for obj in objs:
        xform_shear = Rhino.Geometry.Transform.Shear(plane, vector_x, vector_y, vector_z)    
        xform_rotation = Rhino.Geometry.Transform.Rotation(angle * math.pi / 180, center)    
        scriptcontext.doc.Objects.Transform(obj, xform_rotation * xform_shear, True)
        rs.ObjectName(obj.ObjectId, "")
    print message

__commandname__ = "ObliqueRestoration"

def RunCommand( is_interactive ):
    objs = FindObjectsByName("Oblique Plan")
    if objs != 0:
        CustomTransformation(objs, Rhino.Geometry.Vector3d(1,0,0), Rhino.Geometry.Vector3d(0,1,0), Rhino.Geometry.Vector3d(0,-1,1), -45, "Plan restored")

    objs = FindObjectsByName("Oblique Elevation")
    if objs != 0:
        CustomTransformation(objs, Rhino.Geometry.Vector3d(1,0,0), Rhino.Geometry.Vector3d(-0.707,1,-0.707), Rhino.Geometry.Vector3d(0,0,1), 0, "Elevation restored")
        
    return 0
    
#RunCommand(True)