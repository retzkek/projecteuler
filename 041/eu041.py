#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 41
solution by Kevin Retzke (retzkek@gmail.com), April 2012

Problem 41
==========

We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital
and is also prime.

What is the largest n-digit pandigital prime that exists?

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

if __name__ == "__main__":
    # calculate pandigital sets
    pandigital = {1:"1"}
    for i in range(2,10):
        pandigital[i] = pandigital[i-1] + str(i)
    for i in range(1,10):
        pandigital[i] = set(pandigital[i])
    # calculate primes
    p = primes()
    while p.lastPrime < 1e10:
        p.next()
    #for n in xrange(54321,0,-1):
    #    nstr = str(n)
    #    if n in p.primeset and set(nstr) == pandigital[len(nstr)]:
    #        print n
        
