// project euler (projecteuler.net) problem 22
// solution by Kevin Retzke (retzkek@gmail.com)
// December 2012
package main

import (
	"./tree"
	"bufio"
	"fmt"
	"io"
	"os"
)

func readNames(filename string) (*tree.Tree, error) {
	f, err := os.Open(filename)
	if err != nil {
		return nil, err
	}
	defer f.Close()
	r := bufio.NewReader(f)

	t := tree.NewTreeString()
	for {
		name, err := r.ReadString('\n')
		if err != nil && err != io.EOF {
			return nil, err
		}
		if err == io.EOF {
			break
		}
		t.Insert(name[0 : len(name)-1])
	}
	return t, nil
}

func stringValue(s string) int {
	sum := 0
	for _, c := range s {
		sum += int(c) - int('A') + 1
	}
	return sum
}

func main() {
	names, err := readNames("../data/names_formatted.txt")
	if err != nil {
		fmt.Println(err.Error())
		return
	}
	// generate graphviz file of name tree
	f, err := os.Create("eu022.dot")
	if err != nil {
		fmt.Println(err.Error())
	} else {
		w := bufio.NewWriter(f)
		if err = names.Graphviz(w); err != nil {
			fmt.Println(err.Error())
		}
		w.Flush()
		f.Close()
	}
	// compute name scores
	var tot, i int
	for n := names.First(); n != nil; n = names.Next(n) {
		//fmt.Println(n.Item)
		i++
		tot += stringValue(n.Item.(string)) * i
	}
	fmt.Println(tot)

}
