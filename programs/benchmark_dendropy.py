#! /usr/bin/env python3
from dendropy import Tree
from sys import argv
from time import time

# load
start = time()
tree = Tree.get(path=argv[1], schema='newick')
end = time()
print(end - start)

# preorder
total = 0.
start = time()
for node in tree.preorder_node_iter():
    total += node.edge_length
end = time()
print(end - start)

# postorder
total = 0.
start = time()
for node in tree.preorder_node_iter():
    total += node.edge_length
end = time()
print(end - start)
