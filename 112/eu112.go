// Project Euler (projecteuler.net) Problem 112
// Solution by Kevin Retzke, May 2012
package main

import (
	"fmt"
)

type NumberClass uint

const (
	DECREASING NumberClass = iota
	BOUNCY
	INCREASING
	UNCLASSIFIED
)

func Classify(n int) NumberClass {
	class := UNCLASSIFIED
	lastDigit := n % 10
	n = n / 10
	for n > 0 {
		digit := n % 10
		if digit > lastDigit {
			switch class {
			case INCREASING:
				class = BOUNCY
			case UNCLASSIFIED:
				class = DECREASING
			}
		} else if digit < lastDigit {
			switch class {
			case DECREASING:
				class = BOUNCY
			case UNCLASSIFIED:
				class = INCREASING
			}
		}
		if class == BOUNCY {
			break
		}
		lastDigit = digit
		n = n / 10
	}
	return class
}

func main() {
	/*fmt.Println(Classify(134468)==INCREASING)
	fmt.Println(Classify(66420)==DECREASING)
	fmt.Println(Classify(155349)==BOUNCY)*/
	nBouncy := 0.0
	n := 99
	for nBouncy/float64(n) < 0.99 {
		n++
		if Classify(n) == BOUNCY {
			nBouncy += 1.0
		}
	}
	fmt.Println(n, nBouncy, nBouncy/float64(n))
}
