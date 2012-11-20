#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 25
solution by Kevin Retzke (retzkek@gmail.com), April 2012

Problem #025
============
Starting with the number 1 and moving to the right in a clockwise direction 
a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral 
formed in the same way?

"""
def spiral(n):
    result=1
    lastn=1
    for i in xrange(1,(n-1)/2+1):
        for j in xrange(4):
            lastn = lastn+(i*2)
            result += lastn
    return result
        
         
if __name__ == "__main__":
    import sys
    r=spiral(5)
    if r != 101:
        print "test failed, r=%r" % r
        sys.exit(1)
    print spiral(1001)
