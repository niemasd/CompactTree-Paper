#! /usr/bin/env python3
'''
Run the CompactTree benchmarks
'''

# definitions
EXE_SUFFIX = {
    'CompactTree': '',
    'DendroPy': '_dendropy.py',
    'TreeSwift': '_treeswift.py',
}
MAX_N = {
    'CompactTree': float('inf'),
    'DendroPy': 100000,
    'TreeSwift': 1000000,
}

# imports and check args
from datetime import datetime
from os import chdir, mkdir
from os.path import abspath, dirname, expanduser, isdir, isfile, realpath
from subprocess import DEVNULL, run
from sys import argv, stderr
from tempfile import TemporaryDirectory
assert len(argv) == 2, "USAGE: %s <output_directory>" % argv[0]

# helper function to print log messages
def print_log(s='', end='\n'):
    print("[%s] %s" % (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), s), file=stderr); stderr.flush()

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
    print_log("- Running benchmark: %s" % bench)
    for n in [100, 1000, 10000, 100000]:#, 1000000]:
        print_log("  - Running n = %d" % n)
        n_dir = '%s/n%d' % (outdir, n); mkdir(n_dir)
        for r in range(1, 11):
            print_log("    - Running r = %d" % r)
            tree_fn = '%s/n%d.r%s.nwk' % (n_dir, n, str(r).zfill(2))
            f = open(tree_fn, 'w'); run(['./yule', '1', '-n', str(n)], stdout=f); f.close()
            for tool, tool_suffix in EXE_SUFFIX.items():
                if n > MAX_N[tool]:
                    continue
                print_log("      - Running tool: %s" % tool)
                tool_prefix = '%s.%s' % (tree_fn, tool); f = open('%s.runtime.txt' % tool_prefix, 'w')
                run(['/usr/bin/time', '-v', '-o', '%s.usr_bin_time.txt' % tool_prefix, './%s%s' % (bench, tool_suffix), tree_fn], stdout=f); f.close()
