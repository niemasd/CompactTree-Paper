#! /usr/bin/env python3
from ete4 import Tree
from sys import argv
from time import time
total = 0.
tree = Tree(open(argv[1]), parser=1)
start = time()
for node in tree.traverse('postorder'):
    total += node.dist
end = time()
print(end - start)
