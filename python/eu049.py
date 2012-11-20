#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 49
solution by Kevin Retzke, May 2012
"""
import math

class primes:
    """Calculates prime numbers sequentially."""
    def __init__(self):
        self.primes = [2,3]
        #self.primeset = set(self.primes)
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
        #self.primeset.add(nextPrime)
        self.lastPrime = nextPrime
        return nextPrime

def arePermutations(n,m):
    return set(str(n)) == set(str(m))

if __name__ == '__main__':
    primes = primes()
    while primes.lastPrime < 1e3:
        primes.next()
    primeset = set([primes.lastPrime])
    while primes.lastPrime < 1e4:
        primeset.add(primes.next())
    for n in primeset:
        for p in primeset:
            if p <= n:
                continue
            if arePermutations(n,p):
                p2 = p+p-n
                if p2 in primeset and arePermutations(p2,p):
                    print "%4i%4i%4i" % (n, p, p2)
                    break
