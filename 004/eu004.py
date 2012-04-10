#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 4:
solution by Kevin Retzke (retzkek@gmail.com), April 2009

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

def isPalindrome(num):
    """
    tests if number is palindromic
    """
    str = "%i" % num     # convert number to string
    rev = int(str[::-1]) # reverse and convert back to integer
    return num == rev

def palindrome(digits):
    """
    calculates the largest palindrom made from the product of two digits-digit numbers
    returns the numbers (multiply them to get the palindromic number)
    """
    start = pow(10,digits)-1
    stop = pow(10,digits-1)
    nums=(0,0)
    largest=0

    # naive search multiplying all n-digit numbers and checking if the result is a palindrome
    # note that we need to keep searching even after finding one, since we want the largest,
    # which may not be the first we find (e.g. 999*100 < 998*500)
    for i in range(start,stop-1,-1):
        for j in range(i, stop-1, -1):
            if isPalindrome(i*j) and i*j > largest:
                print "%i (%i * %i)" % (i*j, i, j)
                largest = i*j
                nums = (i,j)
    return nums


if __name__ == '__main__':
    # test case
    (a,b) = palindrome(2)
    if a*b == 9009:
        print "Test: pass"
    else:
        print "Test: fail (numbers = %i, %i; result = %i)" % (a, b, a*b)
    # challenge
    (a,b) = palindrome(3)
    print "Result: %i (%i * %i)" % (a*b, a, b)
