#! /usr/bin/env python3
from ete4 import Tree
from sys import argv
from time import time
start = time()
tree = Tree(open(argv[1]), parser=1)
end = time()
print(end - start)
