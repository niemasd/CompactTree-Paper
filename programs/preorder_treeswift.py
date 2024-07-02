#! /usr/bin/env python3
from sys import argv
from time import time
from treeswift import read_tree_newick
total = 0.
tree = read_tree_newick(argv[1])
start = time()
for node in tree.traverse_preorder():
    total += node.edge_length
end = time()
print(end - start)
