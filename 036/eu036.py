#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 36
solution by Kevin Retzke (retzkek@gmail.com), April 2012

Problem #36
===========
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in 
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include 
leading zeros.)
"""

def isPalindrome(num):
    """
    tests if number is palindromic in decimal and binary
    """
    sd = '{:d}'.format(num)
    sdrev = sd[::-1]
    sb = '{:b}'.format(num)
    sbrev = sb[::-1]
    return sd == sdrev and sb == sbrev

if __name__ == '__main__':
    import sys
    # test case
    if isPalindrome(585):
        print "Test: pass"
    else:
        print "Test: fail"
        sys.exit(1)
    # challenge
    results=[]
    for i in xrange(1000000):
        if isPalindrome(i):
            results.append(i)
    print results
    print sum(results)

