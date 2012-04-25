#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 75
solution by Kevin Retzke (retzkek@gmail.com), April 2012

Problem #75
============
It turns out that 12 cm is the smallest length of wire that can be bent to 
form an integer sided right angle triangle in exactly one way, but there are 
many more examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an 
integer sided right angle triangle, and other lengths allow more than one 
solution to be found; for example, using 120 cm it is possible to form exactly
three different integer sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L ≤ 1,500,000 
can exactly one integer sided right angle triangle be formed?

Note: This problem has been changed recently, please check that you are using
the right parameters.
"""

def triangles(n):
    """
    Returns set of tuples (a,b,c) where the right angle triangle with integral
    length sides (a,b,c) has perimeter n.
    """
    results=set()
    for a in xrange(1,n):
        for b in xrange(1,n-a):
            c = n-a-b
            if a*a+b*b == c*c:
                abc=[a,b,c]
                abc.sort()
                if tuple(abc) not in set(results):
                    results.add(tuple(abc))
    return results

if __name__ == "__main__":
    result = 0
    for i in xrange(12,1500001):
        if i%10000 == 0:
            print i
        if len(triangles(i)) == 1:
            result += 1
    print result
