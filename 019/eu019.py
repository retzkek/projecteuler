#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 19
solution by Kevin Retzke (retzkek@gmail.com), April 2012

Problem #19
============
You are given the following information, but you may prefer to do some 
research for yourself.

    * 1 Jan 1900 was a Monday.
    * Thirty days has September,
      April, June and November.
      All the rest have thirty-one,
      Saving February alone,
      Which has twenty-eight, rain or shine.
      And on leap years, twenty-nine.
    * A leap year occurs on any year evenly divisible by 4, but not on a 
      century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth 
century (1 Jan 1901 to 31 Dec 2000)?
"""

daysInMonth = [31,28,31,30,31,30,31,31,30,31,30,31]

if __name__ == "__main__":
    d = 0
    n  = 0
    for year in range(1900,2001):
        for month in range(1,13):
            if year > 1900 and d%7 == 0:
                n += 1
                print "%i/%i" % (month,year)
            d += daysInMonth[month-1]
            # leap year
            if month == 2 and year%4 == 0:
                if year%100 and not year%400:
                    continue
                d += 1
    print n
