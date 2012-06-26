// project euler (projecteuler.net) problem 23
// Solution by Kevin Retzke, June 2012

#include <stdlib.h>
#include <stdio.h>

typedef unsigned int key_t;

////////////////////////////////////////////////////////////////////////////////
// Binary tree                                                                //
////////////////////////////////////////////////////////////////////////////////

// basic tree node
typedef struct Node {
    key_t key;
    struct Node *lt, *gt;
} node;

// allocate and initialize new node
node*
initNode(key_t key)
{
    node *new = malloc(sizeof(node));
    if (new == NULL) {
        printf("Error. Unable to allocate new node.\n");
        return NULL;
    }
    new->lt = NULL;
    new->gt = NULL;
    new->key = key;
    return new;
}

// Delete node, leaving children. Use delTree() to delete 
// node and all children.
void 
delNode(node *n)
{
    free(n);
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
            n->lt = initNode(key);
            return n->lt;
        } else {
            return addKey(n->lt, key);
        }
    } else {
        // traverse right tree
        if (n->gt == NULL) {
            n->gt = initNode(key);
            return n->gt;
        } else {
            return addKey(n->gt, key);
        }
    }
    return NULL;
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
    node *tree = initNode(tvals[0]);
    for (int i = 1; i < 6; i++) {
        if (addKey(tree, tvals[i]) == NULL) {
            printf("Warning. testTree() failed adding node.\n");
        }
    }
    if (findKey(tree, 75) == NULL) pass=1;
    if (findKey(tree, 1) != NULL) pass=1;
    if (pass != 0) {
        printf("Warning. testTree() failed tests.\n");
    }
    graphvizTree(tree);
    delTree(tree);
    return pass;
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
}
