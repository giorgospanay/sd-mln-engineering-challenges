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

# Network generation. Params:
# 	n - Number of vertices
# 	l - Number of layers
gen_network <- function(n,l){
	e<-sqrt(n)
	p<-e/choose(n,2)
	# Generate multiplex networks of size n
	#Set probability and dependency matrices for networks.
	pr.external <- matrix(0,nrow=l)
	pr.internal <- matrix(1,nrow=l)
	dependency <- diag(l)
	# Choose ER model for each layer.
	models_mix <- c()
	for (i in 1:l){
		models_mix <- c(models_mix,evolution_er_ml(n))
	}
	# Generate network of n actors, n*e edges.
	net<-grow_ml(n,n*e,models_mix,pr.internal,pr.external,dependency)
	return(net)
}

# --- EXTRA FUNCTIONS ---

# Makes sample (one edge) empty network
read_empty <- function(filenames){
  net<-ml_empty()
  # Add edge, as contained in 1000-0-10
  add_layers_ml(net,1:10,rep(TRUE,10))
  add_edge(net,1,17,10)
  return(net)
}

# Add edge (n1,n2,l) to multiplex network net
add_edge <- function(net,n1,n2,l){
	edges<-data.frame(actor1=n1,layer1=l,actor2=n2,layer2=l)
	add_vertices_ml(net,data.frame(actor=n1,layer=l))
	add_vertices_ml(net,data.frame(actor=n2,layer=l))
	add_edges_ml(net,edges)
	return(net)
}

# Remove edge (n1,n2,l) from multiplex network net
rem_edge <- function(net,n1,n2,l){
	edges<-data.frame(actor1=n1,layer1=l,actor2=n2,layer2=l)
	delete_edges_ml(net,edges)
	return(net)
}


# Main function. Used for poster viz
main <- function(){
	#net <- ml_florentine()
	#plot_network(net)
	net<-gen_network(100,5)
	print(net)
}

# if(!interactive()){
# 	main()
# }