#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 27:
solution by Kevin Retzke (retzkek@gmail.com), April 2009

Euler published the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive 
values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 
is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly 
divisible by 41.

Using computers, the incredible formula  n² − 79n + 1601 was discovered, 
which produces 80 primes for the consecutive values n = 0 to 79. The 
product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

    n² + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |−4| = 4

Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n, 
starting with n = 0.

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
    maxcount=0
    #for a in [1,-79]:
    #    for b in [41,1601]:
    for a in xrange(-999,1000):
        for b in xrange(-999,1000):
            n=0
            while True:
                r = n*n+a*n+b
                while r > ps.lastPrime:
                    ps.next()
                if r not in ps.primeset:
                    break
                n += 1
            if n > maxcount:
                print "n^2 + %i*n + %i matches %i primes (a*b=%i)" % (a,b,n,a*b)
                maxcount=n
