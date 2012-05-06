// Project Euler (projecteuler.net) problem 58
// Kevin Retzke (retzkek@gmail.com), May 2012
package main

import (
    "math"
    "fmt"
)

// Primes is a type for containing a list of primes.
type Primes struct {
	Primes []int
    PrimeSet map[int] bool
	Last   int
}

// Init initializes a Primes struct with the first two primes.
func (p *Primes) Init() {
	p.Primes = []int{2, 3}
	p.Last = 3
}

// Next computes, returns, and appends the next prime number.
// Computed via trial division by primes.
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
    p.PrimeSet[next] = true
	p.Last = next
	return next
}

// Eratosthenes populates p with all primes up to max, computed with
// the Sieve of Eratosthenes.
func (p *Primes) Eratosthenes(max int) {
    sieve := make([]bool, max)
    for i := 2; i*i < max; i++ {
        if !sieve[i] {
            for j := 2*i; j < max; j += i {
                sieve[j] = true
            }
        }
    }
	p.Primes = []int{2}
    p.PrimeSet = make(map[int] bool)
    p.PrimeSet[2] = true
    for i := 3; i < max; i++ {
        if !sieve[i] {
            p.Last = i
            p.Primes = append(p.Primes, p.Last)
            p.PrimeSet[p.Last] = true
        }
    }
}

func (p *Primes) IsPrime(n int) bool {
    for n > p.Last {
        p.Next()
    }
    return p.PrimeSet[n]
}

func main() {
    p := new(Primes)
    p.Eratosthenes(100000000)
    side := 3
    nprime := 3.0
    ndiag := 5.0
    lastn := 9
    for nprime/ndiag > 0.1 {
        i := (side-1)/2+1
        for j := 0; j < 4; j++ {
            lastn = lastn+2*i
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
