// project euler (projecteuler.net) problem 14
// solution by Kevin Retzke (retzkek@gmail.com)
// December 2012
package main

import (
	"fmt"
	"os"
)

func seq(n uint) uint {
	if n%2 == 0 {
		return n/2
	}
	return 3*n+1
}

// countToOne returns a closure that will return the length of
// the chain seq(seq(seq(...))) that returns 1.
func countToOne() func(uint) uint {
	count := make(map[uint]uint)
	return func(n uint) uint {
		m := n
		var i uint
		for i = 1; m > 1; i++ {
			m = seq(m)
			if count[m] > 0 {
				i += count[m]
				break
			}
		}
		count[n] = i
		return i
	}
}


func main() {
	c := countToOne()
	if c(13) != 10 {
		fmt.Printf("Test failed. count(13) = %v (should be 10)\n",c(13))
		os.Exit(1)
	}

	var max, imax uint
	for i := uint(1); i < 1e6; i++ {
		if m := c(i); m > max {
			max = m
			imax = i
			//fmt.Println(imax,max)
		}
	}
	fmt.Println(imax)
}
