#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 62
solution by Kevin Retzke, May 2012
"""
import math

def countDigits(n):
    """Returns list of len(10) with number of each digit in n."""
    digits = [0]*10
    while n > 0:
        digits[n%10] += 1
        n = n//10
    return digits

if __name__ == '__main__':
    assert countDigits(345**3) == countDigits(384**3) == \
           countDigits(405**3)
    cubes = []
    for n in xrange(10000):
        cubes.append(countDigits(n**3))
    n = 0
    for c in cubes:
        nperm = 0
        for c2 in cubes:
            if c == c2:
                nperm += 1
        if nperm == 5:
            print n**3
            break
        n += 1

        
