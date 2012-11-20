#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 7
solution by Kevin Retzke (retzkek@gmail.com), April 2009
"""

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

def nthPrime(n, max):
    """
    returns the nth prime number
    due to the sieve we are using, it is necessary to specify a max
    """
    p = primes(max)
    for i in range(n):
        pp = p.next()
    if not pp:
        print "%ith prime not found. increase max." % n
        return -1
    else:
        return pp
    
if __name__ == '__main__':
    # test case
    r = nthPrime(6,100)
    if r == 13:
        print "Test: pass"
    else:
        print "Test: fail (result = %i)" % r
    # challenge
    r = nthPrime(10001,200000)
    print "Result: %i" % r
