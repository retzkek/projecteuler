#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 30
solution by Kevin Retzke (retzkek@gmail.com), April 2012

Problem #30
============
Surprisingly there are only three numbers that can be written as the sum of 
fourth powers of their digits:

    1634 = 14 + 64 + 34 + 44
    8208 = 84 + 24 + 04 + 84
    9474 = 94 + 44 + 74 + 44

As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth 
powers of their digits.
"""
def sumpowers(power,nmax):
    results=[]
    for i in xrange(2,nmax):
        digits=[int(x) for x in str(i)]
        if sum(map(lambda x: pow(x,power),digits))==i:
            results.append(i)
            print i
    return results

        
if __name__ == "__main__":
    import sys
    print "test:"
    r = sum(sumpowers(4,10000))
    if r != 19316:
        print "test failed, r=%r != 19316" % r
        sys.exit(1)
    print "problem:"
    print sum(sumpowers(5,1000000))

