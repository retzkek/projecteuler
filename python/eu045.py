#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 45
solution by Kevin Retzke (retzkek@gmail.com), April 2012
"""

def triangle(n):
    return n*(n+1)/2

def pentagonal(n):
    return n*(3*n-1)/2

def hexagonal(n):
    return n*(2*n-1)

if __name__ == "__main__":
    end = 1000000
    p = set()
    h = set()
    for i in xrange(end):
        p.add(pentagonal(i))
        h.add(hexagonal(i))
    for i in xrange(286,end):
        t = triangle(i)
        if t in p and t in h:
            print t
            break
