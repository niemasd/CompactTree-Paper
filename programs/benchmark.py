#! /usr/bin/env python3
'''
Run the CompactTree benchmarks
'''

# definitions
EXE_SUFFIX = {
    'bigtree':     '_bigtree.py',
    'Biopython':   '_biopython.py',
    'bp':          '_bp.py',
    'CompactTree': '_compact_tree',
    'DendroPy':    '_dendropy.py',
    'ETE':         '_ete.py',
    'scikit-bio':  '_skbio.py',
    'TreeSwift':   '_treeswift.py',
}
MAX_N = {
    'bigtree':          1000000,
    'Biopython':        1000000,
    'bp':              10000000,
    'CompactTree': float('inf'),
    'DendroPy':         1000000,
    'ETE':              1000000,
    'scikit-bio':       1000000,
    'TreeSwift':        1000000,
}

# imports and check args
from datetime import datetime
from os import chdir, mkdir
from os.path import abspath, dirname, expanduser, isdir, isfile, realpath
from subprocess import DEVNULL, run
from sys import argv, stderr
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

# write relevant info about the benchmark
f = open('%s/versions.txt' % outdir, 'w')
run(['pip', 'freeze'], stdout=f)
f.write('compact_tree==%s\n' % [l for l in open('compact_tree.h') if l.strip().startswith('#define VERSION')][0].split()[-1].replace('"',''))
f.close()
f = open('%s/specs.txt' % outdir, 'w')
f.write('=== Operating System Details ===\n'); f.flush()
run(['cat', '/etc/os-release'], stdout=f); f.flush()
f.write('\n'); f.flush()
f.write('=== RAM Details ===\n'); f.flush()
run(['free', '--mega'], stdout=f); f.flush()
f.write('\n'); f.flush()
f.write('=== CPU Details ===\n'); f.flush()
run(['cat', '/proc/cpuinfo'], stdout=f); f.flush()
f.write('\n'); f.flush()
f.close()

# run benchmark
for n in [100, 1000, 10000, 100000, 1000000, 10000000]:
    print_log("  - Running n = %d" % n)
    n_dir = '%s/n%d' % (outdir, n)
    if not isdir(n_dir):
        mkdir(n_dir)
    for r in range(1, 11):
        print_log("    - Running r = %d" % r)
        tree_fn = '%s/n%d.r%s.nwk' % (n_dir, n, str(r).zfill(2))
        print_log("      - Simulating tree...")
        f = open(tree_fn, 'w'); run(['./yule', '1', '-n', str(n)], stdout=f); f.close()
        for tool, tool_suffix in EXE_SUFFIX.items():
            if n > MAX_N[tool]:
                continue
            print_log("      - Running tool: %s" % tool)
            tool_prefix = '%s.%s' % (tree_fn, tool); f = open('%s.runtime.tsv' % tool_prefix, 'w')
            run(['/usr/bin/time', '-v', '-o', '%s.usr_bin_time.txt' % tool_prefix, './benchmark%s' % (tool_suffix), tree_fn], stdout=f); f.close()
