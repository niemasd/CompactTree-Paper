#! /usr/bin/env python3
from dendropy import Tree
from sys import argv
from time import time
start = time()
tree = Tree.get(path=argv[1], schema='newick')
end = time()
print(end - start)
