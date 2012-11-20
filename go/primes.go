// Methods for computing prime numbers.
// Kevin Retzke (retzkek@gmail.com), May 2012
package main

import (
    "math"
    "fmt"
)

// Primes is a type for containing a list of primes.
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
    for i := 3; i < max; i++ {
        if !sieve[i] {
            p.Last = i
            p.Primes = append(p.Primes, p.Last)
        }
    }
}

// Sundaram populates p with all primes up to max, computed with
// the Sieve of Sundaram, an improved Sieve of Eratosthenes.
/*func (p *Primes) Sundaram(max int) {
    sieve := make([]bool, max/2+1)
}*/

func main() {
    p := new(Primes)
    /*p.Init()
    for p.Last < 1e7 {
        p.Next()
    }*/
    p.Eratosthenes(987654321)
    fmt.Println(p.Last)
}
