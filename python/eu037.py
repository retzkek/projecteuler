#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 37
solution by Kevin Retzke (retzkek@gmail.com), April 2012

Problem #37
===========
The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each 
stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 
379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
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

if __name__ == '__main__':
    ps = primes()
    ps.next()
    ps.next()
    results=[]
    while len(results) < 11:
        p = ps.next()
        strp = str(p)
        isTruncatable=True
        # test left
        for i in xrange(1,len(strp)):
            if int(strp[i:]) not in ps.primeset:
                isTruncatable=False
                break
        # test right
        if isTruncatable:
            for i in xrange(len(strp)-1,0,-1):
             if int(strp[:i]) not in ps.primeset:
                 isTruncatable=False
                 break
        if isTruncatable:
            print p
            results.append(p)
    print "Sum: %i" % sum(results)
        
