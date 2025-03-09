# CompactTree-Paper
Repository to store data/figures for CompactTree paper:

> **Moshiri N** (2025). "CompactTree: A lightweight header-only C++ library for ultra-large phylogenetics." *Gigabyte*. [doi:10.46471/gigabyte.152](https://doi.org/10.46471/gigabyte.152)

* **[`programs`](programs)** - Simple programs to benchmark each of the tools
    * **[`programs/benchmark.py`](programs/benchmark.py)** - The main program that runs the entire benchmark
* **[`figures`](figures)** - Directory where the figures will be output
    * **[`figures/figures.py`](figures/figures.py)** - Script that will generate the figures

To run the benchmark:

```bash
git clone --recurse-submodules https://github.com/niemasd/CompactTree-Paper.git
rm -rf results figures/*.pdf
python3 programs/benchmark.py results
python3 figures/figures.py results
```

The benchmark results from the final CompactTree paper can be found on GigaDB ([`raw_benchmark_results.zip`](https://s3.ap-northeast-1.wasabisys.com/gigadb-datasets/live/pub/10.5524/102001_103000/102675/raw_benchmark_results.zip)), and the automatically-generated GitHub Actions outputs can be found in the [most recent Release of this GitHub repo](https://github.com/niemasd/CompactTree-Paper/releases/latest).

## Tools
* [Bio++ bpp-phyl](https://github.com/BioPP/bpp-phyl)
* [bigtree](https://github.com/kayjan/bigtree)
* [Biopython](https://biopython.org/)
* [bp](https://github.com/biocore/improved-octo-waddle)
* [CompactTree](https://github.com/niemasd/CompactTree)
* [DendroPy](https://github.com/jeetsukumaran/DendroPy)
* [ETE](https://github.com/etetoolkit/ete)
* [genesis](https://github.com/lczech/genesis)
* [scikit-bio](https://scikit.bio/)
* [TreeSwift](https://github.com/niemasd/TreeSwift)

## Datasets
Benchmarking was performed on trees simulated under the Yule model with a rate of *λ* = 1 using the [Dual Birth Simulator](https://github.com/niemasd/Dual-Birth-Simulator) ([Moshiri, 2017](https://doi.org/10.1101/226423)).
