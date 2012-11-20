#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 104
solution by Kevin Retzke (retzkek@gmail.com), April 2012

Problem #104
============
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

It turns out that F541, which contains 113 digits, is the first
Fibonacci number for which the last nine digits are 1-9 pandigital
(contain all the digits 1 to 9, but not necessarily in order). And
F2749, which contains 575 digits, is the first Fibonacci number for
which the first nine digits are 1-9 pandigital.

Given that Fk is the first Fibonacci number for which the first nine
digits AND the last nine digits are 1-9 pandigital, find k.
"""

class fib:
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
    ns = fib()
    shouldTest = False
    pandigital = set("123456789")
    while True:
        n = ns.nextn()
        if ns.k == 541:
            print "Test: F541 - Last nine digits are 1-9 pandigital: ",
            if set(str(n%1000000000)) == pandigital:
                print "Pass"
            else:
                print "Fail"
                print nstr
                break
        elif ns.k == 2749:
            print "Test: F2749 - First nine digits are 1-9 pandigital: ",
            if set(str(n)[:9]) == pandigital:
                print "Pass"
            else:
                print "Fail"
                print nstr
                break
            shouldTest = True
        elif shouldTest and set(str(n%1000000000)) == pandigital \
            and set(str(n)[:9]) == pandigital:
            print "Challenge: k=%i" % ns.k
            break
