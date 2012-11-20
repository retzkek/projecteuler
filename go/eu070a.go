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

func countDigits(n int) []int {
    digits := make([]int,10)
    for n > 0 {
        digits[n%10]++
        n = n/10
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

func phi(n int, p Primes) int {
    for _, m := range p.Primes {
        if m > n {
            break
        }
        if n%m == 0 {
            phi *= (1 - 1/float64(m))
        }
    }
    return phi
}

func main() {
    const maxn = 10000000
    const maxij = int(math.Sqrt(float64(maxn)))
    primes := new(Primes)
    primes.Eratosthenes(maxn)
    minn := 0
    minnphin := float64(9999999)
    phis = make(map[int] int)
    for i := 1; i <= maxij; i++ {
        if phis[i] == 0 {
           phis[i] = phi(i) 
        for j := i; j <= maxij*maxij/i; j++ {
            q := primes.Primes[j]
            n := p*q
            phi := float64(n)
            if nphin := float64(n) / phi; nphin < minnphin && 
                arePermutations(n,int(phi)) {
                minn = n
                minnphin = nphin
                fmt.Println(minn,int(phi), minnphin)
            }
        }
    }
}
