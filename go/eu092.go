// project euler (projecteuler.net) problem 92
// solution by Kevin Retzke, May 2012
package main

import (
	"fmt"
)

// SquareDigits returns the sum of the squares of the digits in n.
func SquareDigits(n int) int {
	result := 0
	for ; n > 0; n = n / 10 {
		digit := n % 10
		result += digit * digit
	}
	return result
}

// NumberChain recursively calculates the end result of the number
// chain starting with n.
func NumberChain(n int) int {
	s := SquareDigits(n)
	if s == 1 || s == 89 {
		return s
	}
	return NumberChain(s)
}

func main() {
	if NumberChain(44) != 1 || NumberChain(85) != 89 {
		fmt.Println("Test Failed")
		return
	}
	result := 0
	for n := 1; n < 10000000; n++ {
		if NumberChain(n) == 89 {
			result++
		}
	}
	fmt.Println(result)
}
