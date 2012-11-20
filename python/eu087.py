#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 87
solution by Kevin Retzke, May 2012
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
        #self.primeset = set(self.primes)
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
        #self.primeset.add(nextPrime)
        self.lastPrime = nextPrime
        return nextPrime

if __name__ == '__main__':
    p = primes()
    while p.lastPrime**2 < 50e6:
        p.next()
    sumset = set()
    for p2 in [n*n for n in p.primes if n*n < 50e6]:
        for p3 in [n**3 for n in p.primes if n**3 < 50e6]:
            for p4 in [n**4 for n in p.primes if n**4 < 50e6]:
                n = p2+p3+p4
                if n < 50e6:
                    sumset.add(p2+p3+p4)
    print len(sumset)
