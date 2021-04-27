#!/usr/bin/env python3
"""
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1

"""

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def solve(tree):
    values = []
    def count_unival(tree):
        if is_leaf(tree):
            values.append(tree.value)
            return
        
        left = tree.left
        right = tree.right
        
        if left.value == right.value:
            values.append(left.value)
        
        count_unival(left)
        count_unival(right)
    
    count_unival(tree)
    print(values)
    print(len(values))

def is_leaf(node):
    return node.left is None and node.right is None

if __name__ == '__main__':
    tree = Node(0, Node(1), Node(0))
    tree.right.left = Node(1, Node(1), Node(1))
    tree.right.right = Node(0)
    solve(tree)
