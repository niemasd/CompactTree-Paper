#! /usr/bin/env python3
from Bio import Phylo
from sys import argv
from time import time

# load
start = time()
tree = Phylo.read(argv[1], 'newick')
end = time()
print('load\t%s' % (end - start))

# preorder
total = 0.
start = time()
for node in tree.find_clades(order='preorder'):
    total += node.branch_length
end = time()
print('preorder\t%s' % (end - start))

# postorder
total = 0.
start = time()
for node in tree.find_clades(order='postorder'):
    total += node.branch_length
end = time()
print('postorder\t%s' % (end - start))
