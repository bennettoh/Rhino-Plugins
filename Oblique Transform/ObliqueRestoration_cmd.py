import rhinoscriptsyntax as rs
import Rhino
import scriptcontext
import System.Guid

__commandname__ = "ObliqueRestoration"

def FindObjectsByName(name):
    settings = Rhino.DocObjects.ObjectEnumeratorSettings()
    settings.NameFilter = name
    ids = [rhobj.Id for rhobj in scriptcontext.doc.Objects.GetObjectList(settings)]
    if not ids:
        return 0
    return ids

def RunCommand( is_interactive ):

    origin = (0,0,0)
    point_x = (1,0,0)
    point_y = (0,1,0)
    plane = rs.WorldXYPlane()

    objs = FindObjectsByName("Oblique Plan")
    if objs != 0:
        rs.RotateObject(objs, plane.Origin, 90, plane.YAxis, copy=False)
        rs.ShearObject(objs, origin, point_x, -45, copy=False)
        rs.RotateObject(objs, plane.Origin, -90, plane.YAxis, copy=False)
        rs.RotateObject(objs, origin, -45, None, copy=False)
        rs.ObjectName(objs, "")
        print "Success"

    objs = FindObjectsByName("Oblique Elevation")
    if objs != 0:
        rs.RotateObject(objs, plane.Origin, -135, plane.YAxis, copy=False)
        rs.ShearObject(objs, origin, point_y, -45, copy=False)
        rs.RotateObject(objs, plane.Origin, 135, plane.YAxis, copy=False)
        rs.ObjectName(objs, "")
        print "Success"
    return 0
#RunCommand(True)