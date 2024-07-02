#! /usr/bin/env python3
from Bio import Phylo
from sys import argv
from time import time
start = time()
tree = Phylo.read(argv[1], 'newick')
end = time()
print(end - start)
