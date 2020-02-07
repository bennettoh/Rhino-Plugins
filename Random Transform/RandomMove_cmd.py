import rhinoscriptsyntax as rs
import random

__commandname__ = "RandomMove"

def RunCommand( is_interactive ):

    objs = rs.GetObjects("Select objects to move")
    
    if objs:
        start = rs.GetPoint("Point to move from")
        if start:
            end = rs.GetPoint("Point to move to")
            if end:
                translation = end-start
                for obj in objs:
                    rs.MoveObject(obj, translation * random.random())
    return 0

#RunCommand(True)