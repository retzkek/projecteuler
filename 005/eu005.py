#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 5:
solution by Kevin Retzke (retzkek@gmail.com), April 2009

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers from 1 to 20?
"""

def smallestDivisibleBy(max):
    """
    calculates the smallest number that is evenly divisible by all integers from 1 to max (inclusive)
    """
    i = 0
    found = False
    while not found:
        i += max
        candidate = True
        for j in range(max,int(max/2)-1,-1):
            if i % j != 0:
                candidate = False
                break
        if candidate == True:
            found = True
    return i

if __name__ == '__main__':
    # test case
    r = smallestDivisibleBy(10)
    if r == 2520:
        print "Test: pass"
    else:
        print "Test: fail (result = %i)" % r
    # challenge
    r = smallestDivisibleBy(20)
    print "Result: %i" % r
