#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 6:
solution by Kevin Retzke (retzkek@gmail.com), April 2009

The sum of the squares of the first ten natural numbers is,
1^(2) + 2^(2) + ... + 10^(2) = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^(2) = 55^(2) = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

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
