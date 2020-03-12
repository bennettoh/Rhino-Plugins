from Rhino.Input.Custom import *
import rhinoscriptsyntax as rs
import random

__commandname__ = "RandomMove"

def RunCommand( is_interactive ):
    go = GetObject()
    go.SetCommandPrompt("Select objects to move randomly")
    go.GetMultiple(1, 0)
    objs = go.Objects() #stores objref
    
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