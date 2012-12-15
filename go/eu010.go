// project euler (projecteuler.net) problem 10
// solution by Kevin Retzke (retzkek@gmail.com)
// November 2012
package main

import (
	"./primes"
	"fmt"
)

func sumPrimes(p *primes.Primes, max int) uint64 {
	sum := uint64(0)
	for i := 0; p.Primes[i] < max; i++ {
		sum += uint64(p.Primes[i])
	}
	return sum
}

func main() {
	p := new(primes.Primes)
	p.Init()
	p.Eratosthenes(2500000)

	if sumPrimes(p, 10) != 17 {
		fmt.Println("Test failed. sumPrimes(10) = %d (should be 17)\n", sumPrimes(p, 10))
		return
	}

	fmt.Println(sumPrimes(p, 2e6))
}
