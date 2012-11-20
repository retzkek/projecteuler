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
    # literal implementation; impractical for large p
    a = 0
    for k in range(1,6):
        a += math.factorial(p-k)
    return a%p

def s1(p):
    # simplified to one factorial; still impractical for large p
    a=math.factorial(p-5)*9
    return a%p

def s2(p):
    # same as above, but only keep mod p residual
    a=1
    for i in xrange(2,p-4):
        a *= i
        a = a%p
    return (9*a)%p

def s3(p):
    # simplified via Wilson's Theorem
    # (p-1)! = p-1 (mod p)
    # (p-2)! = 1 (mod p)
    # (p-3)! = (p-1)/2 (mod p)
    # unclear how the following two work when result is not an integer
    # determined formula for those cases via observation
    # (p-4)! = (p+1)/6 (mod p)
    # (p-5)! = (p-1)/24 (mod p)
    a = (p-1) + (p+1) + (p-1)/2
    if (p+1)%6 == 0:
        a += (p+1)/6
    else:
        a += (5*p+1)/6
    if (p-1)%24 == 0:
        a += (p-1)/24
    else:
        a += ((p*p-1)/24)%p
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
    #i = 0
    while p.next() < 1e8:
        tot += s3(p.lastPrime)
        #if i%10000 == 0:
        #    print i,p.lastPrime,tot
        #i += 1
    print tot
