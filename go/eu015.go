// Project Euler problem 15
// Solution by Kevin Retzke
// December 2012
package main

import (
	"fmt"
	"math/big"
)

func factorial(n int) *big.Int {
	fac := new(big.Int)
	fac.MulRange(1, int64(n))
	return fac
}

func paths(n int) *big.Int {
	r := new(big.Int)
	fn := factorial(n)
	r.Div(factorial(2*n), fn.Mul(fn, fn))
	return r
}

func main() {
	fmt.Println(paths(20))
}
