#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 102
solution by Kevin Retzke (retzkek@gmail.com), May 2012
"""
import math

class point:
    """
    Simple 2D point type.
    """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def len(self):
        return math.sqrt(self.x*self.x+self.y*self.y)
    def dot(self,other):
        return self.x*other.x+self.y*other.y
    def angle(self, other):
        return math.acos(self.dot(other)/(self.len()*other.len()))

def containsOrigin(triangle):
    """
    Tests if triangle, defined by list of three points representing the
    three corners, contains the origin.

    Method: compute the angle between each of the three vectors pointing
    from the origin to each of the three corners.  If the sum is 2pi,
    the origin is in the triangle.
    """
    a = triangle[0]
    b = triangle[1]
    c = triangle[2]
    return a.angle(b)+b.angle(c)+c.angle(a)+0.00001 > math.pi*2

if __name__ == "__main__":
    a = point(-340, 495)
    b = point(-153, -910)
    c = point(835, -947)
    assert containsOrigin([a,b,c])
    x = point(-175, 41)
    y = point(-421, -714)
    z = point(574, -645)
    assert not containsOrigin([x,y,z])
    f = open('triangles.txt')
    n = 0
    for line in f:
        pts = map(int,line.split(','))
        a = point(pts[0],pts[1])
        b = point(pts[2],pts[3])
        c = point(pts[4],pts[5])
        if containsOrigin([a,b,c]):
            n += 1
    print n
