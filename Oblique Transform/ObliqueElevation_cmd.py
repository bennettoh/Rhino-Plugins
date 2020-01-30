import rhinoscriptsyntax as rs

__commandname__ = "ObliqueElevation"

def RunCommand( is_interactive ):
    objs = rs.GetObjects("Select objects to be converted to elevation oblique")
    origin = (0,0,0)
    point_y = (0,1,0)
    plane = rs.WorldXYPlane()
    
    if objs:
        rs.RotateObject(objs, plane.Origin, -135, plane.YAxis, copy=False)
        rs.ShearObject(objs, origin, point_y, 45, copy=False)
        rs.RotateObject(objs, plane.Origin, 135, plane.YAxis, copy=False)
        rs.ObjectName(objs, "Oblique Elevation")
        print "Success"
    return 0

#RunCommand(True)