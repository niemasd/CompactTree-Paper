#! /usr/bin/env python3
from sys import argv
from time import time
from treeswift import read_tree_newick
start = time()
tree = read_tree_newick(argv[1])
end = time()
print(end - start)
