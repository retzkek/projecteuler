#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 69
solution by Kevin Retzke, April 2012

inefficient solution, max found so far:
300300 57600 5.21354166667
"""
import math

def gcd(n,m):
    """
    Calculate greatest common divisor of n and m using the 
    Euclidian algorithm.
    """
    if n > m:
        large = n
        small = m
    else:
        large = m
        small = n
    if n==0 or m==0:
        return large
    return gcd(large%small,small)

def phi(n):
    result = 0
    for k in xrange(1,n):
        if gcd(k,n) == 1:
            result += 1
    if result == 0:
        result = 1
    return result

def countDigits(n):
    """Returns list of len(10) with number of each digit in n."""
    digits = [0]*10
    while n > 0:
        digits[n%10] += 1
        n = n//10
    return digits

if __name__ == '__main__':
    maxij = 3163
    phis = {}
    minn = 0
    minnphin = 9999999.0
    for i in xrange(1,maxij+1):
        if i not in phis:
            phis[i] = phi(i)
        for j in xrange(i,maxij*maxij/i):
            if i==j==1:
                continue
            if j not in phis:
                phis[j] = phi(j)
            n = i*j
            gcdij = gcd(i,j)
            phin = phis[i]*phis[j]*gcdij/phis[gcdij]
            nphin = float(n)/phin
            if nphin < minnphin:
                if countDigits(n) == countDigits(phin):
                    minn = n
                    minnphin = nphin
                    print n, nphin
