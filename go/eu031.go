// project euler (projecteuler.net) problem 31
// solution by Kevin Retzke (retzkek@gmail.com), May 2012
package main

import (
	"fmt"
)

func countCombinations(vals []int, total int) int {
	if len(vals) == 0 {
		if total == 0 {
			return 1
		}
		return 0
	}
	count := 0
	if vals[0] <= total {
		count += countCombinations(vals, total-vals[0])
	}
	count += countCombinations(vals[1:], total)
	return count
}

func main() {
	coins := []int{200, 100, 50, 20, 10, 5, 2, 1}
	fmt.Println(countCombinations(coins, 200))
}
