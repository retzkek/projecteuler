#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 32
solution by Kevin Retzke (retzkek@gmail.com), April 2012
"""

if __name__ == "__main__":
    pandigital = set("123456789")
    products = set()
    for i in xrange(10000):
        for j in xrange(i,10000):
            p = i*j
            ns = str(i)+str(j)+str(i*j)
            if len(ns) == 9 and set(ns) == pandigital:
                print i, j, p
                products.add(p)
    print "Sum:", sum(products)
