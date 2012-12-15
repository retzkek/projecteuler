// project euler (projecteuler.net) problem 7
// solution by Kevin Retzke (retzkek@gmail.com), April 2009
package main

import (
	"fmt"
	"./primes"
)

func main() {
	p := new(primes.Primes)
	p.Init()
	for i := 3; i <= 10001; i++ {
		p.Next()
	}
	fmt.Println(p.Last)
}
