#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 85
solution by Kevin Retzke, April 2012
"""

def sumUnder(n):
    return sum(range(n+1))

if __name__ == '__main__':
    target = 2e6
    best = 0
    bestarea = 0
    for i in xrange(100):
        for j in xrange(i):
            nrect = sumUnder(i)*sumUnder(j)
            if abs(target-nrect) < abs(target-best):
                best = nrect
                bestarea = i*j
                print best, i,j, bestarea
