import rhinoscriptsyntax as rs
import Rhino
import scriptcontext
import System.Guid
import Rhino.DocObjects
import math

#    initialize variables
    center = Rhino.Geometry.Point3d(0,0,0)
    vector_x = Rhino.Geometry.Vector3d(1,0,0)
    vector_y = Rhino.Geometry.Vector3d(0,1,0)
    vector_ys = Rhino.Geometry.Vector3d(-0.707,1,-0.707)
    vector_z = Rhino.Geometry.Vector3d(0,-1,1)
    vector_zs = Rhino.Geometry.Vector3d(0,0,1)
    plane = rs.WorldXYPlane()


__commandname__ = "ObliqueRestoration"

def FindObjectsByName(name):
    settings = Rhino.DocObjects.ObjectEnumeratorSettings()
    settings.NameFilter = name
    ids = scriptcontext.doc.Objects.GetObjectList(settings)
    if not ids:
        return 0
    return ids

def RunCommand( is_interactive ):
    objs = FindObjectsByName("Oblique Plan")
    if objs != 0:
        for obj in objs:
            obj_ref = Rhino.DocObjects.ObjRef(obj)
            xform_shear = Rhino.Geometry.Transform.Shear(plane, vector_x, vector_y, vector_z)    
            xform_rotation = Rhino.Geometry.Transform.Rotation(-45 * math.pi / 180, center)    
            scriptcontext.doc.Objects.Transform(obj_ref, xform_rotation * xform_shear, True)
            rs.ObjectName(obj.Id, "")
            print "Plan restored"

    objs = FindObjectsByName("Oblique Elevation")
    if objs != 0:
        for obj in objs:
            obj_ref = Rhino.DocObjects.ObjRef(obj)
            xform_shear = Rhino.Geometry.Transform.Shear(plane, vector_x, vector_ys, vector_zs)
            scriptcontext.doc.Objects.Transform(obj, xform_shear, True)
            rs.ObjectName(obj, "")
        print "Elevation restored"
    return 0
    
#RunCommand(True)
