// project euler (projecteuler.net) problem 70
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

// Eratosthenes populates p with all primes up to max, computed with
// the Sieve of Eratosthenes.
func (p *Primes) Eratosthenes(max int) {
    sieve := make([]bool, max)
    for i := 2; i*i < max; i++ {
        if !sieve[i] {
            for j := 2 * i; j < max; j += i {
                sieve[j] = true
            }
        }
    }
    p.Primes = []int{2}
    for i := 3; i < max; i++ {
        if !sieve[i] {
            p.Last = i
            p.Primes = append(p.Primes, p.Last)
        }
    }
}


func main() {
	p := new(Primes)
	p.Eratosthenes(1000000)
	minn := 999999 
	minnphin := float64(0)
	for n := 2; n <= 10000000; n += 2 {
		phi := float64(n)
		for _, m := range p.Primes {
			if n%m == 0 {
				phi *= (1 - 1/float64(m))
			}
		}
		if nphin := float64(n) / phi; nphin < minnphin {
			minn = n
			minnphin = nphin
			fmt.Println(minn, minnphin)
		}
	}
}
