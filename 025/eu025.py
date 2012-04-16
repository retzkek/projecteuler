#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 25
solution by Kevin Retzke (retzkek@gmail.com), April 2012

Problem #025
============
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn1 + Fn2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?
"""
import operator

class Fib:
    def __init__(self):
        self.nMinus2 = 1
        self.nMinus1 = 1
        self.k = 2
    def nextn(self):
        nextn = self.nMinus2+self.nMinus1
        self.nMinus2 = self.nMinus1
        self.nMinus1 = nextn
        self.k += 1
        return nextn

if __name__ == "__main__":
    ns = Fib()
    while True:
        n=ns.nextn()
        if len(str(n)) == 1000:
            print ns.k
            break
