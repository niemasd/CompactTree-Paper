#! /usr/bin/env python3
from bigtree import newick_to_tree, preorder_iter, postorder_iter
from sys import argv
from time import time

# load
start = time()
tree = newick_to_tree(open(argv[1]).read().strip().rstrip(';'))
end = time()
print(end - start)

# preorder
total = 0.
start = time()
for node in preorder_iter(tree):
    total += node.length
end = time()
print(end - start)

# postorder
total = 0.
start = time()
for node in postorder_iter(tree):
    total += node.length
end = time()
print(end - start)
