# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Design and Implementation

The implementation consists of two classes:

- **`Node`**: Stores a value and references to left and right children.
- **`BST`**: Manages the tree from a root node and provides insertion, search, and in-order traversal.

### Insertion

Values smaller than the current node are placed in the left subtree; larger values go to the right. The method checks for duplicates before inserting to prevent redundant nodes.

### Search

Each comparison eliminates roughly half the remaining nodes, achieving O(log n) average-case time complexity compared to O(n) for linear search in arrays or linked lists.

### In-Order Traversal

Visiting nodes in left-node-right order produces sorted output because all left-subtree values are smaller and all right-subtree values are larger than the current node.

### Edge Cases

- Searching an empty tree returns `False`.
- A single-node tree traverses correctly.
- Duplicate insertions are detected and rejected.

