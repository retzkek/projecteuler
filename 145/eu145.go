// project euler (projecteuler.net) problem 145
// solution by Kevin Retzke, May 2012
package main

import (
	"fmt"
)

// Reverse returns the reverse of n, e.g. Reverse(123)=321.
func Reverse(n int) int {
	// compute reverse of n
	rev := 0
	for ; n > 0; n = n / 10 {
		rev = rev*10 + (n % 10)
	}
	return rev
}

// IsReversible tests if n is reversible, i.e. n+reverse(n) contains
// all odd digits.
func IsReversible(n int) bool {
	// reverse(n) cannot have leading zeros
	if n%10 == 0 {
		return false
	}
	// compute reverse of n
	rev := Reverse(n)
	// test if digits are odd
	for m := n + rev; m > 0; m = m / 10 {
		if (m%10)%2 == 0 {
			return false
		}
	}
	return true
}

func main() {
	result := 0
	for n := 1; n < 1000000000; n++ {
		//fmt.Println(n,Reverse(n))
		if IsReversible(n) {
			result++
		}
	}
	fmt.Println(result)
}
