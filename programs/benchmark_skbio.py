#! /usr/bin/env python3
from skbio.tree import TreeNode
from sys import argv
from time import time

# load
start = time()
tree = TreeNode.read(argv[1])
end = time()
print(end - start)

# preorder
total = 0.
start = time()
for node in tree.preorder():
    total += node.length
end = time()
print(end - start)

# postorder
total = 0.
start = time()
for node in tree.postorder():
    total += node.length
end = time()
print(end - start)
