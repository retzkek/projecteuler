// Project Euler (projecteuler.net) problem 58
// Kevin Retzke (retzkek@gmail.com), May 2012
package main

import (
	"fmt"
	"./primes"
)

func main() {
	p := new(primes.Primes)
	p.Eratosthenes(100000000)
	side := 3
	nprime := 3.0
	ndiag := 5.0
	lastn := 9
	for nprime/ndiag > 0.1 {
		i := (side-1)/2 + 1
		for j := 0; j < 4; j++ {
			lastn = lastn + 2*i
			if p.IsPrime(lastn) {
				nprime += 1.0
			}
		}
		ndiag += 4.0
		side += 2
		//fmt.Println(side, nprime/ndiag, lastn)
	}
	fmt.Println(side)
}
