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
import operator

class ArrayInt:
    def __init__(self,val=0,ndigits=9):
        self.ndigits = ndigits
        self.n = [0]*ndigits
        if val > 0:
            self.setValue(val)
    def setValue(self,val):
        self.n = [int(n) for n in str(val)[-self.ndigits:]]
        if len(self.n) < self.ndigits:
            self.n = [0]*(self.ndigits-len(self.n)) + self.n
    def __add__(self,other):
        new = ArrayInt(self.ndigits)
        new.n = map(operator.add,self.n,other.n)
        for i in range(self.ndigits-1,-1,-1):
            nn = new.n[i]
            if nn > 9:
                new.n[i] = nn%10
                if i > 0:
                    new.n[i-1]+=nn/10
        return new

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

class FibArrayInt:
    def __init__(self):
        self.nMinus2 = ArrayInt(1)
        self.nMinus1 = ArrayInt(1)
        self.k = 2
    def nextn(self):
        nextn = self.nMinus2+self.nMinus1
        self.nMinus2 = self.nMinus1
        self.nMinus1 = nextn
        self.k += 1
        return nextn

if __name__ == "__main__":
    ns = Fib()
    nsarray = FibArrayInt()
    pandigital = set(range(1,10))
    while True:
        last9set = set(nsarray.nextn().n)
        n = ns.nextn()
        if 0 not in last9set and last9set == pandigital:
            print ns.k
            first9set=set([int(a) for a in str(n)[0:9]])
            if first9set==pandigital:
                break
