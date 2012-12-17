package tree

import (
	"errors"
	"fmt"
	"io"
)

// Graphviz produces graphviz dot instructions for graphing
// the tree. Graph with a command like:
//
//     dot FILE.dot -Tpdf -o FILE.pdf
func (t *Tree) Graphviz(w io.Writer) error {
	_, err := fmt.Fprintln(w, "digraph {")
	if err != nil {
		return err
	}
	if t.Root == nil {
		return errors.New("Cannot graph empty tree.")
	}
	if t.graphvizNode(w, t.Root) != nil {
		return err
	}
	_, err = fmt.Fprintln(w, "}")
	return err

}

func (t *Tree) graphvizNode(w io.Writer, n *Node) error {
	if n.left != nil {
		_, err := fmt.Fprintf(w, "\t%v -> %v\n", n.Item, n.left.Item)
		if err != nil {
			return err
		}
		if err = t.graphvizNode(w, n.left); err != nil {
			return err
		}
	}
	if n.right != nil {
		_, err := fmt.Fprintf(w, "\t%v -> %v\n", n.Item, n.right.Item)
		if err != nil {
			return err
		}
		if err = t.graphvizNode(w, n.right); err != nil {
			return err
		}
	}
	return nil
}
