#include <chrono>
#include <iostream>
#include "compact_tree.h"
int main(int argc, char** argv) {
    // load tree
    auto start = std::chrono::system_clock::now();
    compact_tree tree(argv[1]);
    auto end = std::chrono::system_clock::now();
    std::chrono::duration<double> elapsed = end - start;
    std::cout << "load\t" << elapsed.count() << std::endl;

    // preorder
    double total_pre = 0.;
    start = std::chrono::system_clock::now();
    auto it_pre_end = tree.preorder_end();
    for(auto it = tree.preorder_begin(); it != it_pre_end; ++it) {
        total_pre += tree.get_edge_length(*it);
    }
    end = std::chrono::system_clock::now();
    elapsed = end - start;
    std::cout << "preorder\t" << elapsed.count() << std::endl;
    std::cout << "result preorder\t" << total_pre << std::endl;

    // postorder
    double total_post = 0.;
    start = std::chrono::system_clock::now();
    auto it_post_end = tree.postorder_end();
    for(auto it = tree.postorder_begin(); it != it_post_end; ++it) {
        total_post += tree.get_edge_length(*it);
    }
    end = std::chrono::system_clock::now();
    elapsed = end - start;
    std::cout << "postorder\t" << elapsed.count() << std::endl;
    std::cout << "result postorder\t" << total_post << std::endl;
    return 0;
}
