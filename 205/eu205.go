// Project Euler (projecteuler.net) Problem 205
// Solution by Kevin Retzke, May 2012
package main

import (
	"fmt"
	"math"
)

func rolls(ndice, nsides int) map[int]int {
	rs := make(map[int]int)
	for i := 1; i <= nsides; i++ {
		if ndice == 1 {
			rs[i] = 1
		} else {
			for j, n := range rolls(ndice-1, nsides) {
				rs[i+j] += n
			}
		}
	}
	return rs
}

func main() {
	ptotal := math.Pow(4, 9)
	ctotal := math.Pow(6, 6)
	prolls := rolls(9, 4)
	crolls := rolls(6, 6)
	prob := 0.0
	for i, n := range prolls {
		ctot := 0
		for j, m := range crolls {
			if j < i {
				ctot += m
			}
		}
		prob += float64(n) * float64(ctot)
	}
	prob /= (ctotal * ptotal)
	fmt.Printf("%9.7f\n", prob)
}
