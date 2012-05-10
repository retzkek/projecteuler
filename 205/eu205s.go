// Project Euler (projecteuler.net) Problem 205
// Solution by Kevin Retzke, May 2012
package main

import (
	"fmt"
	"math"
	"math/rand"
	"time"
)

func sumDice(ndice, nsides int) int {
	sum := 0
	for d := 0; d < ndice; d++ {
		sum += rand.Intn(nsides) + 1
	}
	return sum
}

func runTrials(nTrials int, c chan int) {
	wins := 0
	for i := 0; i < nTrials; i++ {
		if sumDice(9, 4) > sumDice(6, 6) {
			wins++
		}
	}
	c <- wins
}

func main() {
	const TRIALS = 1000
	const NPROC = 4
	const EPS = 0.0000001
	c := make(chan int)
	var sum float64
	pct, lastPct := 0.0, -1.0
	var i int64
	rand.Seed(time.Now().Unix())
	for math.Abs(pct-lastPct) > EPS {
		i++
		for j := 0; j < NPROC; j++ {
			go runTrials(TRIALS, c)
		}
		for j := 0; j < NPROC; j++ {
			sum += float64(<-c)
		}
		lastPct = pct
		pct = sum / (NPROC * TRIALS * float64(i))
	}
	fmt.Println(pct)
}
