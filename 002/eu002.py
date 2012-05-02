#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 2:
solution by Kevin Retzke (retzkek@gmail.com), April 2009
"""

def fibsum(max):
    fib0=1
    fib1=2
    result=2
    while fib1 < max:
        fibNext=fib0+fib1
        if fibNext < max and fibNext%2 == 0:
            #print fibNext
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
