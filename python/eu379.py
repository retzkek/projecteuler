#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 379
solution by Kevin Retzke, April 2012

Let f(n) be the number of couples (x,y) with x and y positive integers, 
x ≤ y and the least common multiple of x and y equal to n.

Let g be the summatory function of f, i.e.: g(n) = ∑ f(i) for 1 ≤ i ≤ n.

You are given that g(1e6) = 37429395.

Find g(1e12).
"""

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

def lcm(n,m):
    """
    Calculate least common multiple of n and m.
    """
    d = gcd(n,m)
    if d != 0:
        return abs(n*m)/d
    return 0
    

if __name__ == '__main__':
    pass

