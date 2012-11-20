// project euler (projecteuler.net) problem 6:
// solution by Kevin Retzke (retzkek@gmail.com), April 2009
package main

import (
	"fmt"
)

// SumOfSquares calculates the sum of the squares for all natural 
// numbers from 1 to max.
func SumOfSquares(max int) int {
	sum := 0
	for i := 1; i <= max; i++ {
		sum += i * i
	}
	return sum
}

// SquareOfSum calculates the square of the sum for all natural numbers
// from 1 to max.
func SquareOfSum(max int) int {
	sum := 0
	for i := 1; i <= max; i++ {
		sum += i
	}
	return sum * sum
}

func main() {
	// test case
	r := SquareOfSum(10) - SumOfSquares(10)
	if r == 2640 {
		fmt.Println("Test: pass")
	} else {
		fmt.Printf("Test: fail (result = %v)\n", r)
	}
	// challenge
	r = SquareOfSum(100) - SumOfSquares(100)
	fmt.Printf("Result: %v\n", r)
}
