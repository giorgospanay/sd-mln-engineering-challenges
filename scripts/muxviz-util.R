# MuxViz module for paper benchmark code.

# Imports
library(muxViz)

# Loads a network from node/edge/layer files, coded as a config file.
load_net <- function(filenames){
	# # Commented code. MuxViz has a reading bug on this function.
	# net <- buildMultilayerNetworkFromMuxvizFiles(
	# 	paste(data_path,filenames[1],sep=""),				# config file path
	# 	T, 													# is directed
	# 	F,		 											# is weighted
	# 	"ordinal", 											# multislice type
	# 	format="muxviz general", 							# format generic mln
	# 	verbose=F 											# verbose. Set to F
	# )

	# Instead: reading dataframe with only extended edge lists. At the time of writing,
	# 	only way to import a file in the native format. Still reading from config df to
	# 	closely match original format. Operating under assumption that files are in the
	# 	correct format. However, this should be fixed on library
	df_config <- utils::read.table(filenames[[1]],sep=";",header=F)
	colnames(df_config) <- c("layers.file","layer.label.file","layout.file")
	# Reading extended edge list. Also add columns for the later conversion
	df_edges <- utils::read.table(as.character(df_config$layers.file),header=F)
	colnames(df_edges) <- c("node.from","layer.from","node.to","layer.to","weight")
	# Also reading node layout and layer label frames (matching original API call, see
	# 	comments above). This is also to find # of nodes & layers for conversion to SAM
	df_layers <- utils::read.table(as.character(df_config$layer.label.file),header=T)
	l <- nrow(df_layers)
	df_nodes <- utils::read.table(as.character(df_config$layout.file),header=T)
	n <- nrow(df_nodes)
	# Convert dataframe to SupraAdjacencyMatrix
	net_sam <- BuildSupraAdjacencyMatrixFromExtendedEdgelist(
		df_edges,					# dataframe
		l,							# number of layers
		n,							# number of nodes
		T 							# is directed? (Setting to T for benchmark)
	)
	# Spent a good few hours figuring this out. This API needs work.
	# Since, apparently, num of layers and nodes is also needed for validation,
	# 	return array c(net_sam,l,n) and decode later.
	net <- c(net_sam,l,n)
	return(net)
}

build <- function(){

}

build_rem <- function(){

}

# Aggregates a network
aggregate <- function(net){
  net_aggr<-GetAggregateNetworkFromSupraAdjacencyMatrix(
  	net[[1]],						# original net in SAM format
  	net[[2]],						# number of layers
  	net[[3]]						# number of nodes
  )
  return(net_aggr)
}

get_degree <- function(){

}

plot_network <- function(){

}

run_infomap <- function(){

}