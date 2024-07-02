#! /usr/bin/env python3
from sys import argv
from time import time
from treeswift import read_tree_newick

# load
start = time()
tree = read_tree_newick(argv[1])
end = time()
print(end - start)

# preorder
total = 0.
start = time()
for node in tree.traverse_preorder():
    total += node.edge_length
end = time()
print(end - start)

# postorder
total = 0.
start = time()
for node in tree.traverse_postorder():
    total += node.edge_length
end = time()
print(end - start)
