#! /usr/bin/env python3
from ete4 import Tree
from sys import argv
from time import time

# load
start = time()
tree = Tree(open(argv[1]), parser=1)
end = time()
print('load\t%s' % (end - start))
# preorder
total = 0.
start = time()
for node in tree.traverse('preorder'):
    total += node.dist
end = time()
print('preorder\t%s' % (end - start))
print('result preorder\t%s' % total)

# postorder
total = 0.
start = time()
for node in tree.traverse('postorder'):
    total += node.dist
end = time()
print('postorder\t%s' % (end - start))
print('result postorder\t%s' % total)
