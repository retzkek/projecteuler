#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 23
solution by Kevin Retzke (retzkek@gmail.com), April 2012

A perfect number is a number for which the sum of its proper divisors is 
exactly equal to the number. For example, the sum of the proper divisors 
of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest 
number that can be written as the sum of two abundant numbers is 24. By 
mathematical analysis, it can be shown that all integers greater than 28123 
can be written as the sum of two abundant numbers. However, this upper limit 
cannot be reduced any further by analysis even though it is known that the 
greatest number that cannot be expressed as the sum of two abundant numbers 
is less than this limit.

Find the sum of all the positive integers which cannot be written as the 
sum of two abundant numbers.
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
    nmax = 28123
    result = 0
    # abunds contains all abundant numbers less than nmax
    # use a set for the faster membership testing
    abunds = set([i for i in range(12,nmax) if sum(properDivisors(i)) > i])
    for n in range(1,nmax):
        include = True
        for a in abunds:
            if n-a in abunds:
                include = False
                break
        if include:
            result += n
    print result


