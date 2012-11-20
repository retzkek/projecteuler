#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 69
solution by Kevin Retzke, April 2012

inefficient solution, max found so far:
300300 57600 5.21354166667
"""
import math

def gcd(n,m):
    """
    Calculate greatest common divisor of n and m using the 
    Euclidian algorithm.
    """
    if n > m:
        large = n
        small = m
    else:
        large = m
        small = n
    if n==0 or m==0:
        return large
    return gcd(large%small,small)

def phi(n):
    result = 0
    for k in xrange(1,n,2):
        if gcd(k,n) == 1:
            result += 1
    return result

if __name__ == '__main__':
    #assert map(phi, range(2,11)) == [1,2,2,4,2,6,4,6,4]
    result = 0
    maxnphin = 0
    for n in xrange(2,10000,2):
        phin = phi(n)
        if phin > 0:
            nphin = float(n)/phin
            if nphin > maxnphin:
                print n, phin, nphin
                result = n
                maxnphin = nphin
    print result
