#! /usr/bin/env python3
from skbio.tree import TreeNode
from sys import argv
from time import time

# load
start = time()
tree = TreeNode.read(argv[1])
end = time()
print('load\t%s' % (end - start))

# preorder
total = 0.
start = time()
for node in tree.preorder():
    total += node.length
end = time()
print('preorder\t%s' % (end - start))

# postorder
total = 0.
start = time()
for node in tree.postorder():
    total += node.length
end = time()
print('postorder\t%s' % (end - start))
