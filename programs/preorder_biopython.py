#! /usr/bin/env python3
from Bio import Phylo
from sys import argv
from time import time
total = 0.
tree = Phylo.read(argv[1], 'newick')
start = time()
for node in tree.find_clades(order='preorder'):
    total += node.branch_length
end = time()
print(end - start)
