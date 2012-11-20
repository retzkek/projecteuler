// project euler (projecteuler.net) problem 70
// solution by Kevin Retzke (retzkek@gmail.com), May 2012
package main

import (
	"fmt"
	"math"
)

const NCPU = 15

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

func countDigits(n int) []int {
	digits := make([]int, 10)
	for n > 0 {
		digits[n%10]++
		n = n / 10
	}
	return digits
}

func arePermutations(n, m int) bool {
	// test order of magnitude
	//if int(math.Log10(float64(n))) != int(math.Log10(float64(m))) {
	//    return false
	//}
	nlist := countDigits(n)
	mlist := countDigits(m)
	for d := 0; d < 10; d++ {
		if nlist[d] != mlist[d] {
			return false
		}
	}
	return true
}

type Result struct {
	N        int
	Phi      float64
	NOverPhi float64
}

func totient(n int, p *Primes, c chan Result) {
	r := Result{n, float64(n), 1.0}
	for _, m := range p.Primes {
		if m > n {
			break
		}
		if n%m == 0 {
			r.Phi *= (1 - 1/float64(m))
		}
	}
	r.NOverPhi = float64(n) / r.Phi
	c <- r
}

func main() {
	const MAXN = 10000000
	p := new(Primes)
	p.Eratosthenes(MAXN)
	result := Result{0, 0.0, 999999.0}
	c := make(chan Result)
	for n := 3; n <= MAXN; n += 2 * NCPU {
		for nn := n; nn < n+2*NCPU; nn += 2 {
			go totient(nn, p, c)
		}
		//fmt.Println("----------------")
		for i := 0; i < NCPU; i++ {
			r := <-c
			//fmt.Println(r)
			if r.NOverPhi < result.NOverPhi &&
				arePermutations(r.N, int(r.Phi)) {
				result.N = r.N
				result.Phi = r.Phi
				result.NOverPhi = r.NOverPhi
				fmt.Println(result)
			}
		}
	}
}
