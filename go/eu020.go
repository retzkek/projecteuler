// project euler (projecteuler.net) problem 20
// solution by Kevin Retzke (retzkek@gmail.com)
// December 2012
package main

import (
	"fmt"
	"math/big"
	"os"
)

func sumDigitsFac(num int64) int64 {
	n := new(big.Int)
	n.MulRange(1, num)

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
	if r := sumDigitsFac(10); r != 27 {
		fmt.Printf("Test failed. sumDigitsFac(10) = %v (should be 27)\n", r)
		os.Exit(1)
	}
	fmt.Println(sumDigitsFac(100))
}
