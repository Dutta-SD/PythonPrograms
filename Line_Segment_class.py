# -*- coding: utf-8 -*-
"""
Created on Thu May 28 13:56:15 2020

@author: sandi
"""

from abstract_data_type_1 import Point

class LineSegment:
    ''' LineSegment class implements a geometric 
    line segment '''
    def __init__(self, pt1, pt2):
        self.endpointA = pt1
        self.endpointB = pt2
        
    def endpointA(self):
        return self.pt1
    
    def endpointB(self):
        return self.pt2
    
    def __len__(self):
        return self.endpointA.distance_to(endpointB)
    
    def __str__(self):
        return "({}, {}) # ({}, {})".format(
    self.endpointA.getX(),
    self.endpointA.getY(),
    self.endpointB.getX(),
    self.endpointB.getY())
    
    def isVertical(self):
        return (self.endpointA.getX() == self.endpointB.getX())
    
    def isHorizontal(self):
        return (self.endpointA.getY() == self.endpointB.getY())
    
    def slope(self):
        diff = self.endpointA - self.endpointB
        try:
            slope = diff.y / diff.x
        except ZeroDivisionError:
            slope = None
        return slope
        
        
line_1  = LineSegment(Point(3, 5), Point(-2, 7))

print(line_1.slope())