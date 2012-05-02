#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 6:
solution by Kevin Retzke (retzkek@gmail.com), April 2009
"""


def sumOfSquares(max):
    """
    calculates the sum of the squares for all natural numbers from 1 to max
    """
    return sum(map(lambda x: x*x, range(1,max+1)))

def squareOfSum(max):
    """
    calculates the square of the sum for all natural numbers from 1 to max
    """
    n = sum(range(max+1))
    return n*n

if __name__ == '__main__':
    # test case
    r = squareOfSum(10) - sumOfSquares(10)
    if r == 2640:
        print "Test: pass"
    else:
        print "Test: fail (result = %i)" % r
    # challenge
    r = squareOfSum(100) - sumOfSquares(100)
    print "Result: %i" % r
