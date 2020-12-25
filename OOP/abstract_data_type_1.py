# -*- coding: utf-8 -*-
"""
Created on Thu May 28 13:34:04 2020

@author: sandi
"""

# To implement point class
# and Line Segment class


class Point:
    
    '''Point class implements geometric 2D points
    '''
    
    def __init__(self,x, y):
        self.x = x
        self.y = y
    
    def getX(self):
        # Get X coordiante
        return self.x
    
    def getY(self):
        # Get Y coordinate
        return self.y
    
    def distance_to(self, other):
        # Computes Euclidean Distance
        x_diff = self.x - other.x
        y_diff = self.y - other.y
        return (x_diff ** 2 + y_diff ** 2)**0.5
    
    def __eq__(self, other):
        # Check equality
        return ((self.x == other.x) and (self.y == other.y))
    
    def __add__(self, other):
        # Addition of two Points
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        # Subctraction of two Points
        return Point(self.x - other.x, self.y - other.y)
    
    def __repr__(self):
        # representations
        return "class: Point({}, {})".format(self.x, self.y)
    
    def __str__(self):
        # String representation
        return "({}, {})".format(self.x, self.y)
    
    
    
    