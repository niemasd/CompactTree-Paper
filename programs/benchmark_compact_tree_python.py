#! /usr/bin/env python3
from sys import argv
from time import time
from CompactTree import compact_tree, traverse_postorder, traverse_preorder

# load
start = time()
tree = compact_tree(argv[1])
end = time()
print('load\t%s' % (end - start))

# preorder
total = 0.
start = time()
for node in traverse_preorder(tree):
    total += tree.get_edge_length(node)
end = time()
print('preorder\t%s' % (end - start))
print('result preorder\t%s' % total)

# postorder
total = 0.
start = time()
for node in traverse_postorder(tree):
    total += tree.get_edge_length(node)
end = time()
print('postorder\t%s' % (end - start))
print('result postorder\t%s' % total)
