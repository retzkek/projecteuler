#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 50
solution by Kevin Retzke, May 2012
"""
import math

class primes:
    """Calculates prime numbers sequentially."""
    def __init__(self):
        self.primes = [2,3]
        self.primeset = set(self.primes)
        self.lastPrime = 3
    def next(self):
        """calculate and return next prime"""
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
    primes = primes()
    while primes.lastPrime < 1e6:
        primes.next()
    maxterms = 0
    for i in xrange(len(primes.primes)):
        p = primes.primes[i]
        for start in xrange(i-maxterms):
            if sum(primes.primes[start:start+maxterms]) > p:
                break
            for end in xrange(start+maxterms,i):
                s =  sum(primes.primes[start:end])
                if s > p:
                    break
                if s == p and end-start > maxterms:
                    print p, end-start
                    maxterms = end-start
