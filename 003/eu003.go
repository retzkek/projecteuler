// project euler (projecteuler.net) problem 3
// solution by Kevin Retzke (retzkek@gmail.com) April 2012
package main

import (
	"fmt"
)

// LargestPrimeFactor returns the largest prime factor of num.
func largestPrimeFactor(num int64) int64 {
	var result, fac int64 = 1, 2
	for fac*fac <= num {
		if num%fac == 0 && fac > result {
			result = fac
			num = num / fac
		} else {
			fac += 1
		}
	}
	if num != 1 {
		result = num
	}
	return result
}

func main() {
	var r int64
	// test case
	if r = largestPrimeFactor(13195); r == 29 {
		fmt.Println("Test: pass")
	} else {
		fmt.Printf("Test: fail (r=%v)\n", r)
	}
	// challenge
	r = largestPrimeFactor(600851475143)
	fmt.Printf("Result: %v\n", r)
}
