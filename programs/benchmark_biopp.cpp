#include <chrono>
#include <iostream>
#include <memory>
#include <Bpp/Phyl/Io/Newick.h>
#include <Bpp/Phyl/Tree/TreeIterator.h>
using namespace bpp;

// benchmark program
int main(int argc, char** argv) {
    // load tree
    auto start = std::chrono::system_clock::now();
    Newick reader;
    std::unique_ptr<TreeTemplate<Node>> tree = reader.readTreeTemplate(argv[1]);
    auto end = std::chrono::system_clock::now();
    std::chrono::duration<double> elapsed = end - start;
    std::cout << "load\t" << elapsed.count() << std::endl;

    // preorder
    double total_pre = 0.;
    start = std::chrono::system_clock::now();
    PreOrderTreeIterator it_pre(*tree);
    for(const Node* node = it_pre.begin(); node != it_pre.end(); node = it_pre.next()) {
        total_pre += node->getDistanceToFather();
    }
    end = std::chrono::system_clock::now();
    elapsed = end - start;
    std::cout << "preorder\t" << elapsed.count() << std::endl;
    std::cout << "result preorder\t" << std::setprecision(15) << total_pre << std::endl;

    // postorder
    double total_post = 0.;
    start = std::chrono::system_clock::now();
    PostOrderTreeIterator it_post(*tree);
    for(const Node* node = it_post.begin(); node != it_post.end(); node = it_post.next()) {
        total_post += node->getDistanceToFather();
    }
    end = std::chrono::system_clock::now();
    elapsed = end - start;
    std::cout << "postorder\t" << elapsed.count() << std::endl;
    std::cout << "result postorder\t" << std::setprecision(15) << total_post << std::endl;
    return 0;
}
