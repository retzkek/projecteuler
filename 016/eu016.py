#!/usr/bin/python
# encoding: utf-8

def sumDigits(num):
    """
    calculates the sum of the digits of num.
    """
    numstr = "%i" % num
    return reduce(lambda x, y: int(x)+int(y), numstr)


def main():
    # test case
    r = sumDigits(pow(2,15))
    if r == 26:
        print "Test: pass"
    else:
        print "Test: fail (r = %i)" % r
    print sumDigits(pow(2,1000))

if __name__ == "__main__":
    main()
