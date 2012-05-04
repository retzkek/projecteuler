// project euler (projecteuler.net) problem 69
// solution by Kevin Retzke (retzkek@gmail.com), May 2012
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
	for p.Last < 1e6 {
		p.Next()
	}
    maxn := 0
    maxnphin := float64(0)
    for n := 2; n <= 1000000; n+=2 {
        phi := float64(n)
        for _,m := range p.Primes {
            if n%m == 0 {
                phi *= (1-1/float64(m))
            }
        }
        if nphin := float64(n)/phi; nphin > maxnphin {
            maxn = n
            maxnphin = nphin
            fmt.Println(maxn, maxnphin)
        }
    }
}
