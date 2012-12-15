// project euler (projecteuler.net) problem 12
// solution by Kevin Retzke (retzkek@gmail.com)
// November 2012
package main

import (
	"fmt"
	"os"
)

func triangle(n int) int {
	t := 0
	for i := 1; i <= n; i++ {
		t += i
	}
	return t
}

func nFactors(n int) int {
	r := 0
	i := 1
	for i*i < n {
		if n%i == 0 {
			r += 2
		}
		i++
	}
	return r
}

func firstOverNFactors(n int) int {
	var t int
	for i := 0; ; i++ {
		t = triangle(i)
		tf := nFactors(t)
		if tf > n {
			break
		}
	}
	return t
}

func main() {
	if triangle(7) != 28 {
		fmt.Printf("Test failed. triangle(7) = %d (should be 28)\n", triangle(7))
		os.Exit(1)
	}
	if firstOverNFactors(5) != 28 {
		fmt.Printf("Test failed. firstOverNFactors(5) = %d (should be 28)\n",
			firstOverNFactors(5))
		os.Exit(1)
	}
	fmt.Println(firstOverNFactors(500))
}
