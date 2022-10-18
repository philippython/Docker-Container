# 3. Testing of OOP programmes

#  code below are from geom.py
class Coordinate: # coordinate class
     def __init__(self,x,y):
        # make coordinate obj with a reference (self), an x and a y
        self.x=x
        self.y=y
     def distance(self,another): # distance between 2 coordinates
        import math
        xdist=abs(self.x-another.x)
        ydist=abs(self.y-another.y)
        return math.sqrt(xdist**2+ydist**2) # pythagoras theorem