#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 53
solution by Kevin Retzke (retzkek@gmail.com), April 2012
"""
import math

def combinations(n, r):
    return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))

if __name__ == "__main__":
    assert combinations(5,3) == 10
    assert combinations(23,10) == 1144066
    count = 0
    for n in xrange(1,101):
        for r in xrange(1,n+1):
            if combinations(n,r) > 1e6:
                count += 1
                #print n,r,combinations(n,r)
    print count
