# MuxViz module for paper benchmark code.

# Imports
library(muxViz)


# Loads a network from node/edge/layer files into MuxViz. Coded as a config file.
load <- function(filenames){
	# Load from file
	net <- buildMultilayerNetworkFromMuxVizFiles(
		filenames,				# config file path
		T, 						# is directed
		F,		 				# is weighted
		"ordinal", 				# multislice type
		format="muxviz general" # format generic mln
	)
	return(net)
}

build <- function(){

}

build_rem <- function(){

}

# Aggregates a network in MuxViz.
aggregate <- function(net,L,N){
  net_aggr<-GetAggregateNetworkFromSupraAdjacencyMatrix(net,L,N)

}

get_degree <- function(){

}

plot_network <- function(){

}

run_infomap <- function(){

}


# Loads a network from file and aggregates it into a monoplex.
# Time performance, track memory consumption
exp1 <- function(){
	
}



nten<-SupraAdjacencyToNodesTensor(nadj,L,N)
  # Calculate flattening time
  startTime <- Sys.time()
  endTime <- Sys.time()
  print(N)
  print(endTime-startTime)

