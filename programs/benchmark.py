#! /usr/bin/env python3
'''
Run the CompactTree benchmarks
'''

# imports and check args
from os import chdir, mkdir
from os.path import abspath, dirname, expanduser, isdir, isfile, realpath
from subprocess import DEVNULL, run
from sys import argv
from tempfile import TemporaryDirectory
assert len(argv) == 2, "USAGE: %s <output_directory>" % argv[0]

# set things up
outdir = abspath(expanduser(argv[1]))
assert not isfile(outdir) or isdir(outdir), "Output exists: %s" % outdir
mkdir(outdir)
chdir(dirname(realpath(__file__)))
run(['make', 'clean'], stdout=DEVNULL)
run(['make'], stdout=DEVNULL)

# compile Yule simulator
if not isfile('yule'):
    run(['g++', '-Wall', '-pedantic', '-O3', '-std=c++11', '-o', 'yule', '../submodules/Dual-Birth-Simulator/yule.cpp'], stdout=DEVNULL)
    assert isfile('yule'), "ERROR: Failed to compile 'yule'"

# run benchmark
for bench in ['load_tree']:
    for n in [100, 1000, 10000]:#, 100000, 1000000]:
        n_dir = '%s/n%d' % (outdir, n); mkdir(n_dir)
        for r in range(1, 11):
            tree_fn = '%s/n%d.r%s.nwk' % (n_dir, n, str(r).zfill(2))
            f = open(tree_fn, 'w'); run(['./yule', '1', '-n', str(n)], stdout=f); f.close()
            for tool, suffix in [('CompactTree',''), ('TreeSwift','_treeswift.py')]:
                pass # TODO
