// project euler (projecteuler.net) problem 2
// solution by Kevin Retzke (retzkek@gmail.com) April 2012
package main

import (
	"fmt"
)

// Fibsum computes the sum of all even-valued members of the Fibonacci
// sequence below max.
func fibsum(max int) int {
	var fib0, fib1, fibNext, result = 1, 2, 3, 2
	for fib1 < max {
		fibNext = fib0 + fib1
		if fibNext < max && fibNext%2 == 0 {
			result += fibNext
		}
		fib0 = fib1
		fib1 = fibNext
	}
	return result
}

func main() {
	var r int
	// test case
	if r = fibsum(90); r == 44 {
		fmt.Println("Test: pass")
	} else {
		fmt.Printf("Test: fail (r=%v)\n", r)
	}
	// challenge
	r = fibsum(4e6)
	fmt.Printf("Result: %v\n", r)
}
