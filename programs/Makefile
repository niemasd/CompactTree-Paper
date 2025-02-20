# use g++ compiler
CXX=g++
CXXFLAGS?=-Wall -pedantic -std=c++14

# flag specifications for release and debug
RELEASEFLAGS?=$(CXXFLAGS) -O3

# executables
EXES=benchmark_biopp benchmark_compact_tree

# compile
all: $(EXES)
benchmark_biopp: benchmark_biopp.cpp
	$(CXX) $(RELEASEFLAGS) -o benchmark_biopp benchmark_biopp.cpp -lbpp-phyl3 -lbpp-core3
benchmark_compact_tree: compact_tree.h benchmark_compact_tree.cpp
	$(CXX) $(RELEASEFLAGS) -o benchmark_compact_tree benchmark_compact_tree.cpp
clean:
	$(RM) -r $(EXES) *.o
