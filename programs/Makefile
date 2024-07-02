# use g++ compiler
CXX=g++
CXXFLAGS?=-Wall -pedantic -std=c++11

# flag specifications for release and debug
RELEASEFLAGS?=$(CXXFLAGS) -O3

# executables
EXES=load postorder preorder

# compile
all: $(EXES)
load: compact_tree.h load.cpp
	$(CXX) $(RELEASEFLAGS) -o load load.cpp
postorder: compact_tree.h postorder.cpp
	$(CXX) $(RELEASEFLAGS) -o postorder postorder.cpp
preorder: compact_tree.h preorder.cpp
	$(CXX) $(RELEASEFLAGS) -o preorder preorder.cpp
clean:
	$(RM) -r $(EXES) *.o
