#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 2:
solution by Kevin Retzke (retzkek@gmail.com), April 2009

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Find the sum of all the even-valued terms in the sequence which do not exceed four million.

"""

def fibsum(max):
    fib0=1
    fib1=2
    result=2
    while fib1 < max:
        fibNext=fib0+fib1
        if fibNext < max and fibNext%2 == 0:
            print fibNext
            result += fibNext
        fib0=fib1
        fib1=fibNext

    return result


if __name__ == '__main__':
    # test case
    r = fibsum(90)
    if r == 44: # 2+8+34
        print "Test: pass"
    else:
        print "Test: fail (r=%i)" % r
    # challenge
    r = fibsum(4000000)
    print "Result: %i" % r
