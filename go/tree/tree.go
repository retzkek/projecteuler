// Naive binary search tree without balancing.
// Kevin Retzke, December 2012
package tree

type Tree struct {
	lt    CmpFunc
	Count int
	Root  *Node
}

type Node struct {
	Item
	parent, left, right *Node
}

type Item interface{}

type CmpFunc func(a, b Item) bool

// NewTree initializes and returns a new Tree. 
// ltFunc must return true if a < b.
func NewTree(ltFunc CmpFunc) *Tree {
	t := &Tree{lt: ltFunc}
	return t
}

// Insert adds a value to the tree and returns pointer to Node.
func (t *Tree) Insert(v Item) *Node {
	t.Count++
	if t.Root == nil {
		t.Root = &Node{Item: v}
		return t.Root
	}
	return t.insert(t.Root, v)
}

func (t *Tree) insert(n *Node, v Item) *Node {
	if t.lt(v, n.Item) {
		if n.left == nil {
			n.left = &Node{Item: v, parent: n}
			return n.left
		}
		return t.insert(n.left, v)
	} else if t.lt(n.Item, v) {
		if n.right == nil {
			n.right = &Node{Item: v, parent: n}
			return n.right
		}
		return t.insert(n.right, v)
	}
	// Item already in tree
	return n
}

// Remove deletes a value from the tree.
func (t *Tree) Remove(v Item) {
	n := t.Get(v)
	if n != nil {
		t.removeNode(n)
		t.Count--
	}
}

// removeNode deletes a node from the tree.
func (t *Tree) removeNode(n *Node) {
	if n.left != nil && n.right != nil {
		// two children - find in-order successor and move value
		s := t.successor(n)
		n.Item = s.Item
		t.removeNode(s)
	} else if n.left != nil {
		// promote left child
		n.left.parent = n.parent
		t.replaceInParent(n, n.left)
	} else if n.right != nil {
		// promote right child
		n.right.parent = n.parent
		t.replaceInParent(n, n.right)
	} else {
		// no children
		t.replaceInParent(n, nil)
	}
}

// replaceInParent finds the reference to n in its parent and 
// replaces it with o.
func (t *Tree) replaceInParent(n, o *Node) {
	if n.parent != nil {
		if n.parent.left == n {
			n.parent.left = o
		} else {
			n.parent.right = o
		}
	} else if n == t.Root {
		t.Root = o
	}
}

// find smallest sub-node greater than n.
func (t *Tree) successor(n *Node) *Node {
	m := n.right
	if m == nil {
		return m
	}
	for m.left != nil {
		m = m.left
	}
	return m
}

// Find largest sub-node less than n.
func (t *Tree) predecessor(n *Node) *Node {
	m := n.left
	for m.right != nil {
		m = m.right
	}
	return m
}

// Contains tests if value is in the tree.
func (t *Tree) Contains(v Item) bool {
	return t.Get(v) != nil
}

// Get returns the Node representing v, or nil if not found.
func (t *Tree) Get(v Item) *Node {
	n := t.Root
	for n != nil {
		if t.lt(v, n.Item) {
			n = n.left
		} else if t.lt(n.Item, v) {
			n = n.right
		} else {
			return n
		}
	}
	return nil
}

// Min returns the smallest value in the tree.
func (t *Tree) Min() Item {
	n := t.First()
	if n == nil {
		return nil
	}
	return n.Item
}

// Max returns the largest value in the tree.
func (t *Tree) Max() Item {
	n := t.Last()
	if n == nil {
		return nil
	}
	return n.Item
}

// First returns the min-value node in the tree.
func (t *Tree) First() *Node {
	if t.Root == nil {
		return nil
	}
	n := t.Root
	for n.left != nil {
		n = n.left
	}
	return n
}

// Last return the largest-value node in the tree.
func (t *Tree) Last() *Node {
	if t.Root == nil {
		return nil
	}
	n := t.Root
	for n.right != nil {
		n = n.right
	}
	return n
}

// Next returns the node with the next highest value to n.
func (t *Tree) Next(n *Node) *Node {
	if m := t.successor(n); m != nil {
		return m
	}
	if n.parent != nil {
		if n.parent.left == n {
			return n.parent
		}
	}
	return nil
}
