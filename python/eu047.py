#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 47
solution by Kevin Retzke (retzkek@gmail.com), April 2012
"""

def primefacs(num):
    """returns all prime factors of num"""
    facs=set()
    fac=2
    while (fac*fac <= num):
        if num%fac == 0:
            facs.add(fac)
            num = num//fac
        else:
            fac += 1
    if num != 1:
        facs.add(num)
    return facs


if __name__ == '__main__':
    done = False
    n = 1
    while not done:
        if len(primefacs(n)) == 4 and len(primefacs(n+1)) == 4 and \
           len(primefacs(n+2)) == 4 and len(primefacs(n+3)) == 4:
            print n, n+1, n+2, n+4
            n += 3
            done = True
        n += 1
