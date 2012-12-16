// project euler (projecteuler.net) problem 16
// solution by Kevin Retzke (retzkek@gmail.com)
// December 2012
package main

import (
	"fmt"
	"math/big"
	"os"
)

func sumDigitsPow(base, exp int64) int64 {
	b := big.NewInt(base)
	e := big.NewInt(exp)
	n := new(big.Int)

	n.Exp(b, e, nil)

	ten := big.NewInt(10)
	d := new(big.Int)
	var sum int64

	for n.BitLen() > 0 {
		n.DivMod(n, ten, d)
		sum += d.Int64()
	}

	return sum
}

func main() {
	if sumDigitsPow(2, 15) != 26 {
		fmt.Printf("Test failed. sumDigitsPow(2,15) = %v (should be 26)\n",
			sumDigitsPow(2, 15))
		os.Exit(1)
	}
	fmt.Println(sumDigitsPow(2, 1000))
}
