package tree

import (
	"testing"
	"os"
	"fmt"
)

func TestInt(t *testing.T) {
	bt := NewTreeInt()
	ns := []int{10,20,19,4,102,34}
	for _,n := range ns {
		bt.Insert(n)
	}
	if !bt.Contains(10) {
		t.Error("Should contain 10)")
	}
	if !bt.Contains(34) {
		t.Error("Should contain 34)")
	}
	if bt.Contains(24) {
		t.Error("Should not contain 24)")
	}
	if v := bt.Min(); v != 4 {
		t.Errorf("Min should be 4 (is %v)", v)
	}
	if v := bt.Max(); v != 102 {
		t.Errorf("Max should be 102 (is %v)", v)
	}
	bt.Remove(20)
	if bt.Contains(20) {
		t.Error("Should not contain 20)")
	}
}

func TestString(t *testing.T) {
	bt := NewTreeString()
	ss := []string{"foo","bar","baz","fizz","buzz","0xDEADBEEF"}
	for _,s := range ss {
		bt.Insert(s)
	}
	//bt.Graphviz(os.Stdout)
	if v := "foo"; !bt.Contains(v) {
		t.Errorf("Should contain %v)",v)
	}
	if v := "baz"; !bt.Contains(v) {
		t.Errorf("Should contain %v)",v)
	}
	if v := "buzZ"; bt.Contains(v) {
		t.Errorf("Should not contain %v)",v)
	}
	if v := bt.Min(); v != "0xDEADBEEF" {
		t.Errorf("Min should be \"0xDEADBEEF\" (is %v)", v)
	}
	if v := bt.Max(); v != "foo" {
		t.Errorf("Max should be \"foo\" (is %v)", v)
	}
	bt.Remove("fizz")
	if v := "fizz"; bt.Contains(v) {
		t.Errorf("Should not contain %v)",v)
	}
	//bt.Graphviz(os.Stdout)
}

func ExampleTree_Next() {
	bt := NewTreeInt()
	ns := []int{10,20,19,4,102,34}
	for _,n := range ns {
		bt.Insert(n)
	}
	for n := bt.First(); n != nil; n=bt.Next(n) {
		fmt.Println(n.Item)
	}
	// Output:
	// 4
	// 10
	// 19
	// 20
	// 34
	// 102
}

func ExampleTree_Graphviz() {
	bt := NewTreeInt()
	ns := []int{10,20,19,4,102,34}
	for _,n := range ns {
		bt.Insert(n)
	}
	bt.Graphviz(os.Stdout)
	// Output:
	// digraph {
	//	10 -> 4
	//	10 -> 20
	//	20 -> 19
	//	20 -> 102
	//	102 -> 34
	// }
}
