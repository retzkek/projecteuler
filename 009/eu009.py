#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 8:
solution by Kevin Retzke (retzkek@gmail.com), April 2009

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^(2) + b^(2) = c^(2)

For example, 3^(2) + 4^(2) = 9 + 16 = 25 = 5^(2).

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

# premises:
# (1) a + b + c = n
# (2) a^2 + b^2 = c^2
# (3) a < b < c

def main():
    n = 1000
    a = 0
    found = False
    while not found:
        a += 1
        # from (1) and (2), solve for b
        b  = (n*n - 2*n*a)/(2*n - 2*a)
        # solve for c using (1)
        c = n - a - b
        # check if (2) and (3) hold true
        if a*a + b*b == c*c and b > a and  c > b:
            found = True
    print a, b, c
    print a*b*c


if __name__ == '__main__':
    main()
    
