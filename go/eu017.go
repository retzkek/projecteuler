// project euler (projecteuler.net) problem 17
// solution by Kevin Retzke (retzkek@gmail.com)
// December 2012
package main

import (
	"fmt"
	"os"
)

var (
	digits = []string{
		"zero", "one", "two", "three", "four", "five",
		"six", "seven", "eight", "nine", "ten", "eleven",
		"twelve", "thirteen", "fourteen", "fifteen",
		"sixteen", "seventeen", "eighteen", "nineteen"}
	tens = []string{
		"zero", "ten", "twenty", "thirty", "forty",
		"fifty", "sixty", "seventy", "eighty", "ninety"}
)

func numToWords(num int) string {
	var str string
	if num < 20 {
		str += digits[num]
	} else if num < 100 {
		str += tens[num/10]
		if num%10 > 0 {
			str = fmt.Sprintf("%v-%v", str, numToWords(num%10))
		}
	} else if num < 1000 {
		str = fmt.Sprintf("%v hundred", digits[num/100])
		if num%100 > 0 {
			str = fmt.Sprintf("%v and %v", str, numToWords(num%100))
		}
	} else if num < 1000000 {
		str = fmt.Sprintf("%v thousand", digits[num/1000])
		if num%1000 > 0 {
			str = fmt.Sprintf("%v and %v", str, numToWords(num%1000))
		}
	}
	return str
}

func countLetters(str string) int {
	var cnt int
	for _, c := range str {
		if c != ' ' && c != '-' {
			cnt++
		}
	}
	return cnt
}

func main() {
	if r := countLetters(numToWords(342)); r != 23 {
		fmt.Printf("Test failed. countLetters(342) = %v (should be 23)\n", r)
		os.Exit(1)
	}

	if r := countLetters(numToWords(115)); r != 20 {
		fmt.Printf("Test failed. countLetters(115) = %v (should be 20)\n", r)
		os.Exit(1)
	}

	cnt := 0
	for i := 1; i <= 1000; i++ {
		cnt += countLetters(numToWords(i))
	}
	fmt.Println(cnt)
}
