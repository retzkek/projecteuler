#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 92
solution by Kevin Retzke, May 2012
"""
import math

def squareDigits(n):
    digits = map(int, str(n))
    return sum([n*n for n in digits])

def numberChain(n):
    s = squareDigits(n)
    if s == 1 or s == 89:
        return s
    else:
        return numberChain(s)

if __name__ == '__main__':
    assert numberChain(44) == 1
    assert numberChain(85) == 89
    result = 0
    for n in xrange(1,10**7):
        if numberChain(n) == 89:
            result += 1
    print result
     
