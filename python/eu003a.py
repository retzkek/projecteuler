#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 3:
solution by Kevin Retzke (retzkek@gmail.com), April 2009
"""

def primefacs(num):
    """
    returns all prime factors of num
    """
    facs=[]
    fac=2
    while (fac*fac <= num):
        if num%fac == 0:
            facs.append(fac)
            num = num/fac
        else:
            fac += 1
    if num != 1:
        facs.append(num)
        
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
    r = primefacs(600851475143)
    print r
    print "Result: %i" % r[len(r)-1]
