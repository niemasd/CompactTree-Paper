#include <chrono>
#include <iostream>
#include "compact_tree.h"
int main(int argc, char** argv) {
    double total = 0;
    compact_tree tree(argv[1]);
    auto start = std::chrono::system_clock::now();
    auto it_end = tree.preorder_end();
    for(auto it = tree.preorder_begin(); it != it_end; ++it) {
        total += tree.get_edge_length(*it);
    }
    auto end = std::chrono::system_clock::now();
    std::chrono::duration<double> elapsed = end - start;
    std::cout << elapsed.count() << std::endl;
    return 0;
}
