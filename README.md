# CompactTree-Paper
Repository to store data/figures for CompactTree paper.

* **[`programs`](programs)** - Simple programs to benchmark each of the tools
    * **[`programs/benchmark.py`](programs/benchmark.py)** - The main program that runs the entire benchmark
* **[`figures`](figures)** - Directory where the figures will be output
    * **[`figures/figures.py`](figures/figures.py) - Script that will generate the figures

To run the benchmark:

```bash
git clone --recurse-submodules https://github.com/niemasd/CompactTree-Paper.git
rm -rf results figures/*.pdf
python3 programs/benchmark.py results
python3 figures/figures.py results
```

## Tools
* [bigtree](https://github.com/kayjan/bigtree)
* [Biopython](https://biopython.org/)
* [bp](https://github.com/biocore/improved-octo-waddle)
* [CompactTree](https://github.com/niemasd/CompactTree)
* [DendroPy](https://github.com/jeetsukumaran/DendroPy)
* [ETE](https://github.com/etetoolkit/ete)
* [scikit-bio](https://scikit.bio/)
* [TreeSwift](https://github.com/niemasd/TreeSwift)

## Datasets
Benchmarking was performed on trees simulated under the Yule model with a rate of *λ* = 1 using the [Dual Birth Simulator](https://github.com/niemasd/Dual-Birth-Simulator) ([Moshiri, 2017](https://doi.org/10.1101/226423)).
