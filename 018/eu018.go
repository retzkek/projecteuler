// project euler (projecteuler.net) problem 18
// solution by Kevin Retzke (retzkek@gmail.com), November 2012
package main

import (
	"fmt"
	"os"
	"io"
	"bufio"
	"strings"
	"strconv"
	"flag"
)

type Triangle struct {
	rows [][]int
}

// ReadFile reads a triangle from a text file.
// Example (size=4):
//
//	3
//	7 5
//	2 4 6
//	8 5 9 3
func (t *Triangle) ReadFile(filename string, size int) error {
    f, err := os.Open(filename)
    if err != nil {
		return err
	}
    defer f.Close()
	r := bufio.NewReader(f)

	t.rows = make([][]int, size)
	j := 0
    for {
        line, err := r.ReadString('\n')
        if err != nil && err != io.EOF {
			return err
		}
        if err == io.EOF {
			break
		}
		srow := strings.Fields(line)
		row := make([]int, size)
		for i, n := range srow {
			row[i], err = strconv.Atoi(n)
			if err != nil {
				return err
			}
		}
		//fmt.Printf("%v\n",row)
		t.rows[j] = row
		j++
	}
	if debug {
		t.Print()
	}
	return nil
}

// Print prints the triangle to stdout.
func (t *Triangle) Print() {
	for j,row := range t.rows {
		for i := 0; i < len(t.rows)-j; i++ {
			fmt.Printf("  ")
		}
		for i := 0; i < j+1; i++ {
			fmt.Printf("%3d ",row[i])
		}
		fmt.Printf("\n")
	}
}

// MaxPathSum computes the maximum sum of all paths from top to bottom.
// Note that this modifies the triangle in-place.
func (t *Triangle) MaxPathSum() int {
	for i := len(t.rows)-2; i >= 0; i-- {
		for j := 0; j < i+1; j++ {
			if t.rows[i+1][j] > t.rows[i+1][j+1] {
				t.rows[i][j] += t.rows[i+1][j]
			} else {
				t.rows[i][j] += t.rows[i+1][j+1]
			}
		}
		//t.Print()
	}
	return t.rows[0][0]
}

var debug bool
var help bool
var size int

func init() {
		flag.BoolVar(&debug, "debug", false, "enable debug printing")
		flag.BoolVar(&help, "h", false, "show this help")
		flag.IntVar(&size, "s", 0, "triangle size (required)")
}

func main() {
	flag.Parse()
	if help || len(flag.Args()) != 1 || size == 0 {
		fmt.Println("Usage: %v OPTS -s SIZE FILE")
		fmt.Println("Flags:")
		flag.PrintDefaults()
		return
	}
	var t Triangle
	err := t.ReadFile(flag.Args()[0],size)
	if err != nil {
		fmt.Printf("error: %v\n",err)
		return
	}
	fmt.Printf("%d\n",t.MaxPathSum())
}
