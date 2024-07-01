#! /usr/bin/env python3
from skbio.tree import TreeNode
from sys import argv
from time import time
start = time()
tree = TreeNode.read(argv[1])
end = time()
print(end - start)
