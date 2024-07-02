#! /usr/bin/env python3
from ete4 import Tree
from sys import argv
from time import time

# load
start = time()
tree = Tree(open(argv[1]), parser=1)
end = time()
print(end - start)

# preorder
total = 0.
start = time()
for node in tree.traverse('preorder'):
    total += node.dist
end = time()
print(end - start)

# postorder
total = 0.
start = time()
for node in tree.traverse('postorder'):
    total += node.dist
end = time()
print(end - start)
