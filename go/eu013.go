// Project Euler problem 13
// Solution by Kevin Retzke, June 2012
package main

import (
	"bufio"
	"fmt"
	"io"
	"math/big"
	"os"
)

func main() {
	f, err := os.Open("../data/eu013.dat")
	if err != nil {
		os.Exit(1)
	}
	defer f.Close()
	r := bufio.NewReader(f)

	sum := big.NewInt(0)

	for {
		line, err := r.ReadString('\n')
		if err != nil {
			if err == io.EOF {
				break
			}
			os.Exit(1)
		}
		n := new(big.Int)
		n.SetString(line, 10)
		sum.Add(sum, n)
	}
	fmt.Println(sum.String()[0:10])
}
