// Project Euler (projecteuler.net) Problem 205
// Solution by Kevin Retzke, May 2012
package main

import (
	"fmt"
)

func rolls(ndice, nsides int) map[int]int {
	rs := make(map[int]int)
	for i := 1; i <= nsides; i++ {
		if ndice == 1 {
			rs[i] = 1
		} else {
			for j,n := range rolls(ndice-1,nsides) {
				rs[i+j] += n
			}
		}
	}
	return rs
}

func main() {
	total := 0
	for i, n := range rolls(6,6) {
		fmt.Printf("%v: %v\n",i,n)
		total += n
	}
	fmt.Println(total)
	//fmt.Println(rolls(9,4))
}
