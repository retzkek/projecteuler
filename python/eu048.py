#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 48
solution by Kevin Retzke (retzkek@gmail.com), April 2012
"""

if __name__ == "__main__":
    total = 0
    for i in xrange(1,1001):
        total += pow(i,i)
    print str(total)[len(str(total))-10:]
        
        
