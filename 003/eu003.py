#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 3:
solution by Kevin Retzke (retzkek@gmail.com), April 2009
NOTE: THIS IS THEORETICALLY A VALID SOLUTION, BUT IT WILL NOT RUN DUE TO MEMORY REQUIREMENTS

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from math import sqrt

class primes:
    def __init__(self, max):
        self.numbers = range(2, max+1)
        self.primes = []
    def next(self):
        """
        return next prime
        """
        if (self.numbers):
            prime = self.numbers.pop(0)
            self.primes.append(prime)
            self.numbers = [n for n in self.numbers if n % prime]
            return prime
        else:
            return None
    def all(self):
        while self.numbers:
            self.next()
        return self.primes
    
def primefacs(num):
    """
    returns all prime factors of num
    """
    ps = primes(int(sqrt(num))+1)
    facs=[]
    for p in ps.all():
        if num%p == 0:
            facs.append(p)
    return facs


if __name__ == '__main__':
    # test case
    r = primefacs(13195)
    if r[len(r)-1] == 29:
        print "Test: pass"
    else:
        print "Test: fail (factors = ...)" 
        print r
    # challenge
    #r = primefacs(600851475143)
    #print r
    #print "Result: %i" % r[len(r)-1]
    print primefacs(20)
