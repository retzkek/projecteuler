// project euler (projecteuler.net) problem 19
// solution by Kevin Retzke (retzkek@gmail.com)
// December 2012
package main

import (
	"fmt"
)

type Month int

const (
	JANUARY Month = iota
	FEBRUARY
	MARCH
	APRIL
	MAY
	JUNE
	JULY
	AUGUST
	SEPTEMBER
	OCTOBER
	NOVEMBER
	DECEMBER
)

func daysInMonth(mo Month, yr int) int {
	if mo == FEBRUARY {
		if isLeapYear(yr) {
			return 29
		}
		return 28
	} else if mo == APRIL || mo == JUNE || mo == SEPTEMBER || mo == NOVEMBER {
		return 30
	}
	return 31
}

func isLeapYear(yr int) bool {
	// A leap year occurs on any year divisible by four...
	if yr%4 != 0 {
		return false
	}
	// but not on a century unless it is divisible by 400.
	if yr%100 == 0 && yr%400 != 0 {
		return false
	}
	return true
}

func main() {
	d := 1
	n := 0
	for year := 1900; year <= 2000; year++ {
		for month := JANUARY; month <= DECEMBER; month++ {
			if year > 1900 && d%7 == 0 {
				n++
			}
			d += daysInMonth(month, year)
		}
	}
	fmt.Println(n)
}
