#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 1:
solution by Kevin Retzke (retzkek@gmail.com), April 2009

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000
"""

def natmult(bases, max):
    result=0
    for i in range(max):
        for base in bases:
            if i % base == 0:
                result += i
                #print i
                break  # we don't want to double count a number
    return result


if __name__ == '__main__':
    # test case
    r = natmult([3,5], 10)
    if r == 23:
        print "Test: pass"
    else:
        print "Test: fail (r=%i)" % r
    # challenge
    r = natmult([3,5], 1000)
    print "Result: %i" % r
