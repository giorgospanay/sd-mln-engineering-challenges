# netmem R module for paper benchmark code.

# Imports
library(netmem)
library(igraph)

# Load a network into memory
load_net <- function(filenames){
	# Native reading not available in netmem.
	# Instead: construct adjacency matrices for each layer and interlayer.
	# Now we are only dealing with multiplex networks, so interlayers are simply
	# 	id(I) matrices. For an interconnected multilayer, one needs a more clever
	# 	method to represent combinations of multilayers.

	
	# Create empty list to store layers
	layers<-list()
	ln1_flag<-FALSE
	max_node_id<-0
	max_layer_id<-0
	# Start with 1x1 SAM, update later
	sam<-matrix(0,nrow=1,ncol=1)
	# Open multiplex edgefile. Header line: max_node_id,max_layer_id
	fn<-file(filenames[[1]],"r")
	while(TRUE){
		line<-readLines(fn,n=1)
		if(length(line)==0){
			break
		}
	  	
	  	# Check for first line
	  	if(!ln1_flag){
	  		data<-unlist(strsplit(line,","))
	  		max_node_id<-as.integer(data[[1]])
	  		max_layer_id<-as.integer(data[[2]])
	  		ln1_flag<-TRUE
	  		sam<-matrix(0,nrow=max_layer_id*max_node_id,ncol=max_layer_id*max_node_id)
	  		next
	  	}

	  	# Set number of nodes to max_node_id for adjacency matrix creation
	  	num_nodes<-max_node_id

		# Parse line. Format: layer n_src n_dst weight
		data <- unlist(strsplit(line, " "))
		layer <- as.integer(data[[1]])
		node1 <- as.integer(data[[2]])
		node2 <- as.integer(data[[3]])
		weight <- as.numeric(data[[4]])
  		
  		# Update the supra adjacency matrix with the edge weight
  		sam[(layer-1)*max_node_id+node1,(layer-1)*max_node_id+node2]<-weight
	}

	# When done: add coupling edges for common vertices in layers.
	# 	Basically, complete interlayers. Assume coupling edge weight=1
	for(nid in 1:max_node_id){
		for(lid in 1:max_layer_id-1){
			for (lid2 in lid:max_layer_id){
				sam[(lid-1)*max_node_id+nid,(lid2-1)*max_node_id+nid]<-1
			}
		}
	}

	# Return vector of adjacency matrices
	return(sam)
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
	degs<-gen_degree(net,weighted=TRUE,digraph=FALSE)
	return(degs)
}

# Visualize the network
plot_network <- function(net){
	# Not available in netmem
	return()
}

# Run InfoMap
run_infomap <- function(net){
	# Not available in netmem
	return()
}

# Network generation. Params:
# 	n - Number of vertices
# 	l - Number of layers
gen_network <- function(n,l){
	# Calculate for n*l vertices.
	e<-sqrt(n)
	p<-e/choose(n*l,2)
	# # Taking absurdly long time to generate network, plus unnecessary prints. 
	# net<-ind_rand_matrix(n*l,l=e,digraph=FALSE)

	# Instead: generate own adjacency matrices with igraph for each layer
	sam<-matrix(0,nrow=n*l,ncol=n*l)
	for (lid in 1:l){
		# Generate ERG for each layer
		er<-erdos.renyi.game(n,n*e,type="gnm",directed=FALSE)
		nadj<-as_adj(er,sparse=FALSE)
		# ...and add edges to each layer
		for (i in 1:n){
			for (j in 1:n){
				if (isTRUE(nadj[i,j]==1)){
					sam[(lid-1)*n+i,(lid-1)*n+j]<-1
					sam[(lid-1)*n+j,(lid-1)*n+i]<-1
				}
			}
		}
	}
	# Finally, create multiplex identity matrices for coupling edges
	for(nid in 1:n){
		for(lid in 1:l){
			for (lid2 in 1:l){
				sam[(lid-1)*n+nid,(lid2-1)*n+nid]<-1
			}
		}
	}	
	return(sam)
}

#
# -----------------------------------------------------------------------------
# 


# Main function. 
main <- function(){
	net<-gen_network(10,2)
	print(dim(net))
}

if(!interactive()){
	main()
}