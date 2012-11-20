#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 46
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
    p = primes()
    while p.lastPrime < 1e6:
        p.next()
    squares = [n*n for n in range(1,100)]
    for n in xrange(3,1000000,2):
        if n in p.primeset:
            continue
        found = False
        for ns in [n-2*s for s in squares if n-2*s > 0]:
            if ns in p.primeset:
                found = True
                break
        if not found:
            print n
            break
