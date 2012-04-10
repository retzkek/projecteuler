#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 10:
solution by Kevin Retzke (retzkek@gmail.com), April 2009
SHOULD WORK, BUT IS SLOW! HAVE NOT RUN TO COMPLETION

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

class primes:
    def __init__(self, max):
        self.numbers = [2]+range(3, max+1, 2) # no need to include even numbers greater than 2
        self.primes = []
    def next(self):
        """
        return next prime
        """
        if (self.numbers):
            prime = self.numbers.pop(0)
            self.primes.append(prime)
            self.numbers = [n for n in self.numbers if n % prime]
            print "prime: %i" % prime
            return prime
        else:
            return None
    def all(self):
        while self.numbers:
            self.next()
        return self.primes
   
def sumPrimes(max):
    """
    returns all sum of all prime numbers less than max
    """
    ps = primes(max)
    return sum(ps.all())


if __name__ == '__main__':
    # test case
    r = sumPrimes(10)
    if r == 17:
        print "Test: pass"
    else:
        print "Test: fail (result = %i)" % r 
    # challenge
    r = sumPrimes(2000000)
    print "Result: %i" % r
