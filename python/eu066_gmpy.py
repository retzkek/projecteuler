#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 66
solution by Kevin Retzke, May 2012
"""
import math
import gmpy

def diophantine(d):
    """Determines the minimum solution of x for the equation
    x**2 - Dy**2 = 1"""
    x = gmpy.mpz(2)
    while True:
        num = x*x-1
        if num%d == 0 and gmpy.is_square(num/d):
            return x
        x += 1

if __name__ == '__main__':
    assert map(diophantine, [2,3,5,6,7]) == [3,2,9,5,8]
    maxx = 0
    maxd = 0
    for d in xrange(2,62):
        if gmpy.is_square(d):
            continue
        x = diophantine(d)
        print d, x
        if x > maxx:
            maxx = x
            maxd = d
            #print maxd, maxx
    print maxd
            
