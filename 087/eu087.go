// project euler (projecteuler.net) problem 87
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
	for p.Last*p.Last < 50e6 {
		p.Next()
	}
    p2 := make([]int, len(p.Primes))
    p3 := make([]int, len(p.Primes))
    p4 := make([]int, len(p.Primes))
    for i,p := range p.Primes {
        p2[i] = p*p
        p3[i] = p2[i]*p
        p4[i] = p3[i]*p
    }
    sumset := make(map[int] bool)
    for _,a := range p2 {
        for _,b := range p3 {
            if b > 50e6 {
                break
            }
            for _,c := range p4 {
                if c > 50e6 {
                    break
                }
                sum := a+b+c
                if sum < 50e6 {
                    sumset[sum] = true
                }
            }
        }
    }
	fmt.Println(len(sumset))
}
