#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 56
solution by Kevin Retzke (retzkek@gmail.com), April 2012
"""
def sumDigits(n):
    digits = map(int,str(n))
    return sum(digits)

if __name__ == "__main__":
    maxsum = 0
    for a in xrange(1,100):
        for b in xrange(1,100):
            s = sumDigits(pow(a,b))
            if s > maxsum:
                maxsum = s
                #print a, b, s
    print maxsum
