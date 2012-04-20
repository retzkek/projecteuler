#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 35
solution by Kevin Retzke (retzkek@gmail.com), April 2009

Problem #35
===========
The number, 197, is called a circular prime because all rotations of the 
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 
37, 71, 73, 79, and 97.

How many circular primes are there below one million?
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

def rotations(n):
    strn=str(n)
    lenn=len(strn)
    rotations=[]
    for i in xrange(1,lenn):
        rotations.append(''.join([strn[j%lenn] for j in xrange(i,i+lenn)])) 
    return rotations

if __name__ == '__main__':
    ps = primes()
    while ps.lastPrime < 1000000:
        ps.next()
    results=[]
    for p in ps.primes:
        addresult=True
        for prot in rotations(p):
            if int(prot) not in ps.primeset:
                addresult=False
                break
        if addresult:
            results.append(p)
    print results
    print len(results)
