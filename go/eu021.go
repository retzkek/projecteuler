// project euler (projecteuler.net) problem 21
// solution by Kevin Retzke (retzkek@gmail.com)
// December 2012
package main

import (
	"fmt"
	"os"
)

func sumProperDivisors(n int) int {
	sum := 1
	for fac := 2; fac*fac <= n; fac++ {
		if n%fac == 0 {
			sum += fac
			if fac*fac != n {
				sum += n / fac
			}
		}
	}
	return sum
}

func main() {
	if r := sumProperDivisors(220); r != 284 {
		fmt.Printf("Test failed. sumProperDivisors(220) = %v (should be 284)\n", r)
		os.Exit(1)
	}
	if r := sumProperDivisors(284); r != 220 {
		fmt.Printf("Test failed. sumProperDivisors(284) = %v (should be 220)\n", r)
		os.Exit(1)
	}

	max_n := 10000
	sums := make([]int, max_n)
	for i := 2; i < max_n; i++ {
		sums[i] = sumProperDivisors(i)
	}
	var sum int
	for i := 2; i < max_n; i++ {
		if sums[i] < max_n {
			if sums[i] != i && sums[sums[i]] == i {
				sum += i
			}
		}
	}
	fmt.Println(sum)
}
