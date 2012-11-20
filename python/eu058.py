#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 58
solution by Kevin Retzke (retzkek@gmail.com), April 2012
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
    def isPrime(self, n):
        while n > self.lastPrime:
            self.next()
        return n in self.primeset

if __name__ == "__main__":
    p = primes()
    side = 3
    nprime = 3.0
    ndiag = 5.0
    lastn = 9
    while nprime/ndiag > 0.11:
        i = (side-1)/2+1
        for j in xrange(4):
            lastn = lastn+(i*2)
            if p.isPrime(lastn):
                nprime += 1.0
        ndiag += 4
        side += 2
        print side, nprime/ndiag, lastn
    print side
