# multinet R module for paper benchmark code.

# Imports
library(igraph)
library(multinet)

# Load a network into memory
load_net <- function(filenames){
	net <- read_ml(filenames[[1]])
	return(net)
}

# 
build_rem <- function(filenames){

}

# Aggregate all layers in an aspect
aggregate <- function(net){
	# Retrieve all layers
	all_layers <- layers_ml(net)
	# Aggregate them via flattening. Flattening of individual layers available
	net_aggr <- flatten_ml(net,layers=all_layers)
	return(net_aggr)
}

# Get degree distribution of all actors
get_degree <- function(net){
	degs=degree_ml(net)
	return(degs)
}

# Visualize the network
plot_network <- function(net){
	plot(net)
}

# Run InfoMap
run_infomap <- function(net){
	commstruct=infomap_ml(net,directed=TRUE)
	return(commstruct)
}

# Main function. Used for poster viz
main <- function(){
	net <- ml_florentine()
	plot_network(net)
}

# if(!interactive()){
# 	main()
# }