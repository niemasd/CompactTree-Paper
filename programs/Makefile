# use g++ compiler
CXX=g++
CXXFLAGS?=-Wall -pedantic -std=c++11

# flag specifications for release and debug
RELEASEFLAGS?=$(CXXFLAGS) -O3

# executables
EXES=load_tree

# compile
all: $(EXES)
load_tree: compact_tree.h load_tree.cpp
	$(CXX) $(RELEASEFLAGS) -o load_tree load_tree.cpp
clean:
	$(RM) -r $(EXES) *.o
