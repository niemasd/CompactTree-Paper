#! /usr/bin/env Rscript
library(ape)

# load (initially in "cladewise" order)
start <- Sys.time()
tree <- read.tree(commandArgs(trailingOnly = TRUE)[1])
end <- Sys.time()
cat("load", end-start, sep="\t")
cat("\n")

# preorder
total <- 0.
start <- Sys.time()
tree <- reorder(tree, "postorder")
for(i in nrow(tree$edge):1) {
    total <- total + tree$edge.length[i]
}
end <- Sys.time()
cat("preorder", end-start, sep="\t")
cat("\n")
cat("result preorder", total, sep="\t")
cat("\n")

# reorder back to default "cladewise" order (otherwise postorder traversal has unfair advantage)
tree <- reorder(tree, "cladewise")

# postorder
total <- 0.
start <- Sys.time()
tree <- reorder(tree, "postorder")
for(i in 1:nrow(tree$edge)) {
    total <- total + tree$edge.length[i]
}
end <- Sys.time()
cat("postorder", end-start, sep="\t")
cat("\n")
cat("result postorder", total, sep="\t")
cat("\n")
