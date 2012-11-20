#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 38
solution by Kevin Retzke (retzkek@gmail.com), April 2012

Problem #38
============
Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, 
and 5, giving the pandigital, 918273645, which is the concatenated product 
of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as 
the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

def catProduct(m,n):
    result=''
    for i in xrange(1,n+1):
        result += str(m*i)
    return result

if __name__ == "__main__":
    import sys
    pandigital = set("123456789")
    # test 1
    if set(catProduct(192,3)) != pandigital:
        print "Test 1: fail"
        sys.exit(1)
    # test 2
    if set(catProduct(9,5)) != pandigital:
        print "Test 2: fail"
        sys.exit(1)
    largest=0
    for i in xrange(1,1000000):
        for n in xrange(1,1000000):
            cp = catProduct(i,n)
            icp = int(cp)
            if icp > 999999999:
                break
            if set(cp) == pandigital and icp > largest:
                print cp
                largest = icp
