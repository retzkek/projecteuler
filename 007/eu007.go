// project euler (projecteuler.net) problem 7
// solution by Kevin Retzke (retzkek@gmail.com), April 2009
package main

import (
	"fmt"
	"math"
)

type Primes struct {
	Primes []int
	Last   int
}

// Init initializes a Primes struct with the first two primes.
func (p *Primes) Init() {
	p.Primes = []int{2, 3}
	p.Last = 3
}

// Next computes, returns, and appends the next prime number.
func (p *Primes) Next() int {
	next := 0
	i := p.Last + 2
	for next == 0 {
		sqrti := math.Sqrt(float64(i))
		isPrime := true
		for _, p := range p.Primes {
			if i%p == 0 {
				isPrime = false
				i += 2
				break
			}
			if float64(p) > sqrti {
				break
			}
		}
		if isPrime {
			next = i
		}
	}
	p.Primes = append(p.Primes, next)
	p.Last = next
	return next
}

func main() {
	p := new(Primes)
	p.Init()
	for i := 3; i <= 10001; i++ {
		p.Next()
	}
	fmt.Println(p.Last)
}
