#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 381
solution by Kevin Retzke (retzkek@gmail.com), April 2012

Problem #381
===========
For a prime p let S(p) = (∑(p-k)!) mod(p) for 1 ≤ k ≤ 5.

For example, if p=7,
(7-1)! + (7-2)! + (7-3)! + (7-4)! + (7-5)! = 6! + 5! + 4! + 3! + 2! 
= 720+120+24+6+2 = 872.
As 872 mod(7) = 4, S(7) = 4.

It can be verified that ∑S(p) = 480 for 5 ≤ p < 100.

Find ∑S(p) for 5 ≤ p < 10^8.
"""
import math

def s(p):
    a=math.factorial(p-5)*(pow(p,4)-9*pow(p,3)+27*p*p-30*p+9)
    return a%p

def s1(p):
    a=math.factorial(p-5)*9
    return a%p

def s2(p):
    a=9*((p-1)-24)
    return a%p

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
    tot = 0
    while p.next() < 100:
        tot += s2(p.lastPrime)
    print tot
