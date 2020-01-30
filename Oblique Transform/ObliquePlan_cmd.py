import rhinoscriptsyntax as rs

__commandname__ = "ObliquePlan"

def RunCommand( is_interactive ):
    
    objs = rs.GetObjects("Select objects to be converted to plan oblique")
    origin = (0,0,0)
    point_x = (1,0,0)
    plane = rs.WorldXYPlane()
    
    if objs:
        rs.RotateObject(objs, origin, 45, None, copy=False)
        rs.RotateObject(objs, plane.Origin, 90, plane.YAxis, copy=False)
        rs.ShearObject(objs, origin, point_x, 45, copy=False)
        rs.RotateObject(objs, plane.Origin, -90, plane.YAxis, copy=False)
        rs.ObjectName(objs, "Oblique Plan")
        print "Success"
    return 0
#RunCommand(True)