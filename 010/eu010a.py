#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 10:
solution by Kevin Retzke (retzkek@gmail.com), April 2009

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import sys
import math

class primes:
    """
    Calculates prime numbers sequentially.

    METHODS

    next()      returns the next prime
    """
    def __init__(self):
        self.primes = [2,3]
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
        self.lastPrime = nextPrime
        return nextPrime
   
def sumPrimes(max):
    """
    returns sum of all prime numbers less than max
    """
    ps = primes()
    result = 5
    while True:
        p = ps.next()
        if p > max:
            break
        result += p
    return result


if __name__ == '__main__':
    # test case
    r = sumPrimes(10)
    if r == 17:
        print "Test: pass"
    else:
        print "Test: fail (result = %i)" % r 
        sys.exit(1)
    # challenge
    r = sumPrimes(2000000)
    print "Result: %i" % r
