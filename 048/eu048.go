// Project Euler problem 48
// Solution by Kevin Retzke, June 2012
package main

import (
	"fmt"
)

// TruncInt stores a truncated integer.
type TruncInt struct {
	Digits    []int
	Precision int
}

// Print TruncInt value.
func (t *TruncInt) PrintValue() {
	for i := t.Precision - 1; i >= 0; i-- {
		fmt.Printf("%d", t.Digits[i])
	}
	fmt.Println()
}

// Init initializes a TruncInt type.
func (t *TruncInt) Init(value, precision int) {
	t.Digits = make([]int, precision)
	t.Precision = precision
	for i := 0; i < precision; i++ {
		t.Digits[i] = value % 10
		value = value / 10
	}
}

// Add o to t, results in t.
func (t *TruncInt) Add(o *TruncInt) {
	precision := t.Precision
	if o.Precision < precision {
		precision = o.Precision
	}
	for i := 0; i < precision-1; i++ {
		t.Digits[i] = t.Digits[i] + o.Digits[i]
		t.Digits[i+1] += t.Digits[i] / 10
		t.Digits[i] = t.Digits[i] % 10
	}
	if precision < t.Precision {
		t.Digits[precision] = t.Digits[precision-1] / 10
	}
	t.Digits[precision-1] = (t.Digits[precision-1] + o.Digits[precision-1]) % 10
}

// powmod computes the last digits of base**expo
func powmod(base, expo, digits int) TruncInt {
	var base_t, res_t TruncInt
	base_t.Init(base, digits)
	res_t.Init(base, digits)
	// expand base**expo into base*base*base*...
	for e := 1; e < expo; e++ {
		var tmp_t TruncInt
		tmp_t.Init(0, digits)
		// perform long multiplication
		for i := 0; i < digits; i++ {
			for j := 0; j < digits-i; j++ {
				tmp_t.Digits[i+j] += res_t.Digits[j] * base_t.Digits[i]
			}
		}
		// carry and copy to result array
		for i := 0; i < digits-1; i++ {
			tmp_t.Digits[i+1] += tmp_t.Digits[i] / 10
			res_t.Digits[i] = tmp_t.Digits[i] % 10
		}
		res_t.Digits[digits-1] = tmp_t.Digits[digits-1] % 10
	}
	return res_t
}

func main() {
	res_digits := 10
	var res TruncInt
	res.Init(0, res_digits)
	for i := 1; i < 1000; i++ {
		tmp := powmod(i, i, res_digits)
		res.Add(&tmp)
	}
	res.PrintValue()
}
