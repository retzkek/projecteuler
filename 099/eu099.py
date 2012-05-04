#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 99
solution by Kevin Retzke (retzkek@gmail.com), May 2012
"""
import math

if __name__ == "__main__":
    f = open('base_exp.txt')
    maxline = 0
    maxval = 0.0
    n = 0
    for line in f:
        n += 1
        base, exp = map(int,line.split(','))
        val = exp*math.log(base)
        if val > maxval:
            maxline = n
            maxval = val
    print maxline, maxval
