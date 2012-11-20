#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 63
solution by Kevin Retzke (retzkek@gmail.com), April 2012
"""

if __name__ == "__main__":
    count = 0
    for n in xrange(100):
        m = 0
        while True:
            m += 1
            a = m**n
            lena = len(str(a))
            if lena == n:
                print a
                count += 1
            if lena > n:
                break
    print count
