// project euler (projecteuler.net) problem 23
// Solution by Kevin Retzke, June 2012

#include <stdlib.h>
#include <stdio.h>

////////////////////////////////////////////////////////////////////////////////
// Binary search tree                                                         //
// Implements basic add/remove functionality, no balancing.                   //
////////////////////////////////////////////////////////////////////////////////

typedef unsigned int key_t;

// basic tree node
typedef struct _node {
    key_t key;
	//val_t val;
    struct _node *par, *lt, *gt;
} node;

// allocate and initialize new node
node*
initNode(key_t key, node* parent)
{
    node *new = malloc(sizeof(node));
    if (new == NULL) {
        printf("Error. Unable to allocate new node.\n");
        return NULL;
    }
	new->par = parent;
	new->lt = NULL;
	new->gt = NULL;
    new->key = key;
    return new;
}

// Find smallest sub-node greater than n.
node*
successor(node *n)
{
	node *curr = n->gt;
	if (curr == NULL) return NULL;
	while (curr->lt != NULL) {
		curr = curr->lt;
	}
	return curr;
}

// Find largest sub-node less than n.
node*
predecessor(node *n)
{
	node *curr = n->lt;
	if (curr == NULL) return NULL;
	while (curr->gt != NULL) {
		curr = curr->gt;
	}
	return curr;
}

// Find n in its parent and replace with new.
void
replaceInParent(node *n, node *new)
{
	if (n->par != NULL) {
		if (n->par->lt == n) {
			n->par->lt = new;
		} else {
			n->par->gt = new;
		}
	}
}

// Delete node, rearranging tree as necessary.
void 
delNode(node *n)
{
	if (n->lt != NULL && n->gt != NULL) {
		// two children -- find in-order successor and move value
		node *s = successor(n);
		n->key = s->key;
		delNode(s);
	} else if (n->lt != NULL || n->gt != NULL) {
		// one child -- promote it
		node *ch = n->lt != NULL ? n->lt : n->gt;
		ch->par = n->par;
		replaceInParent(n,ch);
		free(n);
	} else {
		// no children
		replaceInParent(n,NULL);
		free(n);
	}
}

// Delete node and all children.
void
delTree(node *n)
{
    if (n->lt != NULL) delTree(n->lt);
    if (n->gt != NULL) delTree(n->gt);
    free(n);
}

// Add new node to tree. Returns pointer to node, or NULL if error.
node*
addKey(node *n, key_t key)
{
    if (key == n->key) {
        // found value already in tree
        return n;
    } else if (key < n->key) {
        // traverse left tree
        if (n->lt == NULL) {
            n->lt = initNode(key, n);
            return n->lt;
        } else {
            return addKey(n->lt, key);
        }
    } else {
        // traverse right tree
        if (n->gt == NULL) {
            n->gt = initNode(key, n);
            return n->gt;
        } else {
            return addKey(n->gt, key);
        }
    }
    return NULL;
}

// Return smallest node in tree.
node*
first(node *tree)
{

}

// Return largest node in tree.
node*
maxKey(node *tree)
{
}

// Test if tree has key.  Returns pointer to node if found, NULL otherwise.
node*
findKey(node *n, key_t key)
{
    if (key == n->key) {
        return n;
    } else if (key < n->key) {
        // traverse left tree
        if (n->lt != NULL) {
            return findKey(n->lt, key);
        }
    } else {
        // traverse right tree
        if (n->gt != NULL) {
            return findKey(n->gt, key);
        }
    }
    return NULL;
}

// Remove key from tree.
void
delKey(node *tree, key_t key)
{
	node *n = findKey(tree, key);
	if (n != NULL) {
		delNode(n);
	}
}

// Generate graphviz instruction for graphing node to stdout.
void
graphvizNode(node *n)
{
    if (n->lt != NULL) {
        printf("\t%u -> %u\n",n->key, n->lt->key);
        graphvizNode(n->lt);
    }
    if (n->gt != NULL) {
        printf("\t%u -> %u\n",n->key, n->gt->key);
        graphvizNode(n->gt);
    }
}

// Generate graphviz instruction for graphing tree to stdout.
void
graphvizTree(node *n)
{
    printf("digraph {\n");
    graphvizNode(n);
    printf("}\n");
}

// Test tree routines. Returns 0 if success.
int
testTree()
{
    int pass = 0;
    key_t tvals[] = {23, 16, 75, 92, 44, 123};
    node *tree = initNode(tvals[0], NULL);
    for (int i = 1; i < 6; i++) {
        if (addKey(tree, tvals[i]) == NULL) {
            printf("Warning. testTree() failed adding node.\n");
        }
    }
    if (findKey(tree, 75) == NULL) pass=1;
    if (findKey(tree, 1) != NULL) pass=1;
    //graphvizTree(tree);
	delKey(tree, 75);
    //graphvizTree(tree);
    if (findKey(tree, 75) != NULL) pass=1;

    if (pass != 0) {
        printf("Warning. testTree() failed tests.\n");
    }
    delTree(tree);
    return pass;
}

////////////////////////////////////////////////////////////////////////////////
// Utility                                                                    //
////////////////////////////////////////////////////////////////////////////////
int
sumProperDivisors(int n)
{
	int sum = 1;
	int fac = 2;
	while (fac*fac <=n) {
		if (n%fac == 0) {
			sum += fac;
			if (fac*fac != n) {
				sum += n/fac;
			}
		}
		fac++;
	}
	return sum;
}
    
////////////////////////////////////////////////////////////////////////////////
// Main                                                                       //
////////////////////////////////////////////////////////////////////////////////
int
main()
{
    // make sure I didn't break something in the tree along the way
    if (testTree() != 0) {
        return 1;
    }
	// test that 28 is perfect number
	int s = sumProperDivisors(28);
	if (s != 28) {
		printf("Error. sumProperDivisors(28) = %d, expecting 28.\n",s);
		return 1;
	}
	// problem
	
}
