#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 34
solution by Kevin Retzke (retzkek@gmail.com), April 2012

Problem #34
============
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of 
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
import math

def sumDigitFactorial(n):
    result=0
    for d in [int(x) for x in str(n)]:
        result += math.factorial(d)
    return result

if __name__ == "__main__":
    import sys
    print "test:"
    r = sumDigitFactorial(145)
    if r != 145:
        print "test failed, r=%r != 145" % r
        sys.exit(1)
    else:
        print "test passed"
    print "problem:"
    r = 0
    for i in xrange(3,100000):
        if sumDigitFactorial(i) == i:
            print i
            r += i
    print r

