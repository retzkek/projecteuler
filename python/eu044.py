#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 44
solution by Kevin Retzke (retzkek@gmail.com), April 2012
"""

def pentagonal(n):
    return n*(3*n-1)/2

if __name__ == "__main__":
    ps = []
    for i in xrange(1,10000):
        ps.append(pentagonal(i))
    pset = set(ps)
    for i in range(len(ps)):
        for j in range(i,len(ps)):
            m = ps[i]
            n = ps[j]
            if n != m and (m+n) in pset and (n-m) in pset:
                print m, n, n-m
