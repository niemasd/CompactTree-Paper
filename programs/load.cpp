#include <chrono>
#include <iostream>
#include "compact_tree.h"
int main(int argc, char** argv) {
    auto start = std::chrono::system_clock::now();
    compact_tree tree(argv[1]);
    auto end = std::chrono::system_clock::now();
    std::chrono::duration<double> elapsed = end - start;
    std::cout << elapsed.count() << std::endl;
    return 0;
}
