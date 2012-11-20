#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 21
solution by Kevin Retzke (retzkek@gmail.com), April 2012
"""

def properDivisors(n):
    """
    Calculate all proper divisors of n.
    """
    facs = [1]
    fac = 2
    while fac*fac <= n:
        if n%fac == 0:
            facs.append(fac)
            if fac*fac != n:
                facs.append(n/fac)
        fac += 1
    return facs

if __name__ == "__main__":
    sums={}
    for i in xrange(2,10000):
        sums[i] = sum(properDivisors(i))
    amicables=set()
    for n,s in sums.iteritems():
        if s in sums:
            if n != s and sums[s] == n:
                amicables.add(n)
    print amicables
    print sum(amicables)
