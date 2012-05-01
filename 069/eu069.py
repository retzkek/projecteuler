#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 69
solution by Kevin Retzke, April 2012

inefficient solution, max found so far:
300300 57600 5.21354166667
"""
import math

class primes:
    """
    Calculates prime numbers sequentially.

    METHODS

    next()      returns the next prime
    """
    def __init__(self):
        self.primes = [2,3]
        self.primeset = set(self.primes)
        self.lastPrime = 3
    def next(self):
        """
        calculate and return next prime
        """
        nextPrime = None
        i = self.lastPrime+2
        while nextPrime is None:
            sqrt_i = math.sqrt(i)
            isPrime = True
            for p in self.primes:
                if i%p == 0:
                    isPrime = False
                    i += 2
                    break
                if p > sqrt_i:
                    break
            if isPrime:
                nextPrime = i
        self.primes.append(nextPrime)
        self.primeset.add(nextPrime)
        self.lastPrime = nextPrime
        return nextPrime

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
    return result

if __name__ == '__main__':
    assert map(phi, range(2,11)) == [1,2,2,4,2,6,4,6,4]
    #p = primes()
    #while p.lastPrime < 100000:
    #    p.next()
    result = 0
    maxnphin = 0
    for n in xrange(100,1000000,100):
        #if n in p.primeset:
        #    continue
        phin = phi(n)
        if phin > 0:
            nphin = float(n)/phin
            if nphin > maxnphin:
                print n, phin, nphin
                result = n
                maxnphin = nphin
    print result
