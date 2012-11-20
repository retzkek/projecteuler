#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 52
solution by Kevin Retzke (retzkek@gmail.com), April 2012
"""

if __name__ == "__main__":
    x = 0
    while True:
        x += 1
        xset = set(str(x))
        if set(str(2*x)) != xset:
            continue
        if set(str(3*x)) != xset:
            continue
        if set(str(4*x)) != xset:
            continue
        if set(str(5*x)) != xset:
            continue
        if set(str(6*x)) != xset:
            continue
        break
    print x, 2*x, 3*x, 4*x, 5*x, 6*x
