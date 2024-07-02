#! /usr/bin/env python3
from bigtree import newick_to_tree
from sys import argv
from time import time
start = time()
tree = newick_to_tree(open(argv[1]).read().strip().rstrip(';'))
end = time()
print(end - start)
