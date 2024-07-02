#! /usr/bin/env python3
from bigtree import newick_to_tree, postorder_iter
from sys import argv
from time import time
total = 0.
tree = newick_to_tree(open(argv[1]).read().strip().rstrip(';'))
start = time()
for node in postorder_iter(tree):
    total += node.length
end = time()
print(end - start)
