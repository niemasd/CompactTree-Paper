#! /usr/bin/env python3
from skbio.tree import TreeNode
from sys import argv
from time import time
total = 0.
tree = TreeNode.read(argv[1])
start = time()
for node in tree.postorder():
    total += node.length
end = time()
print(end - start)
