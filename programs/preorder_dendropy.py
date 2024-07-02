#! /usr/bin/env python3
from dendropy import Tree
from sys import argv
from time import time
total = 0.
tree = Tree.get(path=argv[1], schema='newick')
start = time()
for node in tree.preorder_node_iter():
    total += node.edge_length
end = time()
print(end - start)
