# netmem R module for paper benchmark code.

# Imports
library(netmem)

# Load a network into memory
load_net <- function(filenames){
	# Native reading not available in netmem.
	# Instead: construct adjacency matrices for each layer and interlayer.
	# Now we are only dealing with multiplex networks, so interlayers are simply
	# 	id(I) matrices. For an interconnected multilayer, one needs a more clever
	# 	method to represent combinations of multilayers.

	file=read.delim("filenamepath",header=FALSE)

}

# 
build_rem <- function(filenames){

}

# Aggregate all layers in an aspect
aggregate <- function(net){
	# Not available in netmem
	return()
}

# Get degree distribution of all actors
get_degree <- function(net){
	
	return()
}

# Visualize the network
plot_network <- function(net){
	# Not available in netmem
	return()
}

# Run InfoMap
run_infomap <- function(net){
	# Not available in netmem
}

# Main function. 
main <- function(){
	
}

if(!interactive()){
	main()
}