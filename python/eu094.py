#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 94
solution by Kevin Retzke, May 2012
"""
import math

if __name__ == '__main__':
    result = 0
    for n in range(2,333333333):
        b = 1.0 + n
        h = math.sqrt(n**2-(b/2)**2)
        a = h*b/2
        if a == float(int(a)):
            result += 3*n+1
    print result
