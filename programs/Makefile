# use g++ compiler
CXX=g++
CXXFLAGS?=-Wall -pedantic -std=c++11

# flag specifications for release and debug
RELEASEFLAGS?=$(CXXFLAGS) -O3

# executables
EXES=benchmark_compact_tree

# compile
all: $(EXES)
benchmark_compact_tree: compact_tree.h benchmark_compact_tree.cpp
	$(CXX) $(RELEASEFLAGS) -o benchmark_compact_tree benchmark_compact_tree.cpp
clean:
	$(RM) -r $(EXES) *.o
