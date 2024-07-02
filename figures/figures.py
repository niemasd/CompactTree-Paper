#! /usr/bin/env python3
'''
Create figures from CompactTree benchmark results
'''

# definitions
TITLE = {
    'mem':       'Peak Memory Usage',
    'load':      'Load Tree',
    'preorder':  'Pre-Order Traversal',
    'postorder': 'Post-Order Traversal',
}
UNIT = {
    'mem':       'MB',
    'load':      'seconds',
    'preorder':  'seconds',
    'postorder': 'seconds',
}
LABEL = {
    'mem':       'Peak Memory Usage',
    'load':      'Runtime',
    'preorder':  'Runtime',
    'postorder': 'Runtime',
}

# imports and check args
from glob import glob
from matplotlib import rcParams
from matplotlib.lines import Line2D
from os import chdir
from os.path import abspath, dirname, expanduser, isdir, realpath
from seaborn import pointplot, set_context, set_style
from sys import argv
import matplotlib.pyplot as plt
assert len(argv) == 2, "USAGE: %s <benchmark_results_output_directory>" % argv[0]

# set things up
argv[1] = abspath(expanduser(argv[1]))
assert isdir(argv[1]), "Directory not found: %s" % argv[1]
outdir = dirname(realpath(__file__))
chdir(outdir)
set_context("paper", rc={"font.size":12,"axes.titlesize":16,"axes.labelsize":14,"legend.fontsize":10,"xtick.labelsize":10,"ytick.labelsize":10})
set_style("ticks")
rcParams['font.family'] = 'serif'

# load data
DATA = {bench:dict() for bench in TITLE}
for fn in glob('%s/*/*.*' % argv[1]):
    # parse metadata from filename
    if fn.endswith('.nwk'):
        continue
    n = int(fn.split('/')[-1].split('.')[0][1:])
    tool = fn.split('/')[-1].split('.nwk.')[1].split('.')[0]

    # handle /usr/bin/time -v output (peak memory)
    if fn.endswith('.usr_bin_time.txt'):
        if n not in DATA['mem']:
            DATA['mem'][n] = dict()
        if tool not in DATA['mem'][n]:
            DATA['mem'][n][tool] = list()
        DATA['mem'][n][tool].append(float([l for l in open(fn) if l.strip().startswith('Maximum resident set size (kbytes)')][0].split()[-1]) / 1000)

    # handle the program output (runtimes for each benchmark)
    elif fn.endswith('.runtime.tsv'):
        for l in open(fn):
            bench, v = [x.strip() for x in l.split('\t')]
            if n not in DATA[bench]:
                DATA[bench][n] = dict()
            if tool not in DATA[bench][n]:
                DATA[bench][n][tool] = list()
            DATA[bench][n][tool].append(float(v))

    # shouldn't reach here
    else:
        assert False, "Invalid results file: %s" % fn

# create figures
TOOLS = sorted(set(k for bench in DATA for n in DATA[bench] for k in DATA[bench][n]))
for bench in DATA:
    x = list(); y = list(); h = list()
    for n in sorted(DATA[bench].keys()):
        for tool in sorted(DATA[bench][n].keys()):
            y += DATA[bench][n][tool]
            x += [n] * len(DATA[bench][n][tool])
            h += [tool] * len(DATA[bench][n][tool])
    fig = plt.figure()
    pointplot(x=x, y=y, hue=h)
    plt.yscale('log')
    plt.title(TITLE[bench])
    plt.xlabel('Number of Leaves')
    plt.ylabel('%s (%s)' % (LABEL[bench], UNIT[bench]))
    #plt.legend(bbox_to_anchor=(0.005, 0.995), loc=2, borderaxespad=0., frameon=True)
    plt.legend(borderaxespad=0., frameon=True)
    fig.savefig('%s.pdf' % bench, format='pdf', bbox_inches='tight')
