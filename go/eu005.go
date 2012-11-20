// project euler (projecteuler.net) problem 5:
// solution by Kevin Retzke (retzkek@gmail.com), April 2009
package main

import (
	"fmt"
)

// Calculates the smallest number that is evenly divisible by all 
// integers from 1 to max (inclusive).
func smallestDivisibleBy(max int) int {
	i := 0
	found := false
	for !found {
		i += max
		candidate := true
		for j := max; j > max/2-1; j-- {
			if i%j != 0 {
				candidate = false
				break
			}
		}
		if candidate {
			found = true
		}
	}
	return i
}

func main() {
	// test case
	r := smallestDivisibleBy(10)
	if r == 2520 {
		fmt.Println("Test: pass")
	} else {
		fmt.Printf("Test: fail (result = %v)\n", r)
	}
	// challenge
	r = smallestDivisibleBy(20)
	fmt.Printf("Result: %v\n", r)
}
