#! /usr/bin/env python3
from bp import parse_newick
from sys import argv
from time import time

# load
start = time()
tree = parse_newick(open(argv[1]).read())
end = time()
print('load\t%s' % (end - start))

# preorder
total = 0.
start = time()
for i in range(len(tree)):
    total += tree.length(tree.preorderselect(i))
end = time()
print('preorder\t%s' % (end - start))
print('result preorder\t%s' % total)

# postorder
total = 0.
start = time()
for i in range(len(tree)):
    total += tree.length(tree.postorderselect(i))
end = time()
print('postorder\t%s' % (end - start))
print('result postorder\t%s' % total)
