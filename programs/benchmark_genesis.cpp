#include <chrono>
#include <iomanip>
#include <iostream>
#include "genesis/genesis.hpp"
using namespace genesis;
using namespace genesis::tree;
int main(int argc, char** argv) {
    // load tree
    auto start = std::chrono::system_clock::now();
    auto const tree = CommonTreeNewickReader().read(utils::from_file(std::string(argv[1])));
    auto end = std::chrono::system_clock::now();
    std::chrono::duration<double> elapsed = end - start;
    std::cout << "load\t" << elapsed.count() << std::endl;

    // preorder
    double total_pre = 0.;
    start = std::chrono::system_clock::now();
    for(auto const& e : preorder(tree)) {
        total_pre += e.edge().data<CommonEdgeData>().branch_length;
    }
    end = std::chrono::system_clock::now();
    elapsed = end - start;
    std::cout << "preorder\t" << elapsed.count() << std::endl;
    std::cout << "result preorder\t" << std::setprecision(15) << total_pre << std::endl;

    // postorder
    double total_post = 0.;
    start = std::chrono::system_clock::now();
    for(auto const& e : postorder(tree)) {
        total_post += e.edge().data<CommonEdgeData>().branch_length;
    }
    end = std::chrono::system_clock::now();
    elapsed = end - start;
    std::cout << "postorder\t" << elapsed.count() << std::endl;
    std::cout << "result postorder\t" << std::setprecision(15) << total_post << std::endl;
    return 0;
}
