# MuxViz module for paper benchmark code.

# Imports
library(muxViz)
library(rgl)
library(ggplot2)
# External imports
###################################################################
## PLOT FUNCTIONS
###################################################################
requireNamespace("graphics", quietly = TRUE)
requireNamespace("grid", quietly = TRUE)
requireNamespace("rgl", quietly = TRUE)
requireNamespace("ggplot2", quietly = TRUE)


# Loads a network from node/edge/layer files, coded as a config file.
load_net <- function(filenames){
	# # Commented code. MuxViz has a bug on this function on the current version.
	# net <- buildMultilayerNetworkFromMuxvizFiles(
	# 	filenames[1],				# config file path
	# 	T, 							# is directed
	# 	F,		 					# is weighted
	# 	"ordinal", 					# multislice type
	# 	format="muxviz general", 	# format generic mln
	# 	verbose=F 					# verbose. Set to F
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
		F 							# is directed? (Setting to F for benchmark.)
	)
	# Spent a good few hours figuring this out. This API needs work.
	# Since num of layers and nodes is also needed for validation,
	# 	return array c(net_sam,l,n) and decode later.
	net <- c(net_sam,l,n)
	return(net)
}


build_rem <- function(){

}

# Aggregates an aspect of the network
aggregate <- function(net){
	net_aggr<-GetAggregateNetworkFromSupraAdjacencyMatrix(
		net[[1]],						# original net in SAM format
		net[[2]],						# number of layers
		net[[3]]						# number of nodes
	)
	return(net_aggr)
}

# Get degree distribution from the network
get_degree <- function(net){
	degs<-GetMultiDegree(
		net[[1]],						# original net in SAM format
  		net[[2]],						# number of layers
  		net[[3]],						# number of nodes
  		F 								# is directed? (set to F for benchmark)
	)
}


plot_network <- function(net,sam){
	# # Convert to network list for visualization
	# sam <- SupraAdjacencyToNetworkList(
	# 	net[[1]],						# original net in SAM format
 #  		net[[2]],						# number of layers
 #  		net[[3]]						# number of nodes
 #  	)
  	# Randomly select L colors for visualization
  	color <- grDevices::colors()[grep('gr(a|e)y', grDevices::colors(), invert = T)]
  	col <- sample(color, net[[2]])

	# Plot multiplex.
	plot_multiplex3D_fix(sam, col)
}

# Run InfoMap community detection
run_infomap <- function(){
	# Path for InfoMap 0.x binary, required by MuxViz.
	# NOTE: Change accordingly for own setup.
	pathInfomap <- "../bin/infomap-0.x/Infomap"

	# Get communities
	commResult <- GetMultilayerCommunities_Infomap(
		net[[1]],						    # original net in SAM format
  	net[[2]],						    # number of layers
  	net[[3]],						    # number of nodes
		bin.path=pathInfomap,		# InfoMap binary path
		isDirected=F 					  # directed = F
	)
	return(commResult)
}

# Auxiliary for plotting
sam_to_netlist <- function(net){
	NodesTensor <- SupraAdjacencyToNodesTensor(
		net[[1]],						# original net in SAM format
  	net[[2]],						# number of layers
  	net[[3]]						# number of nodes
  )
  g.list<-list()
  for (l in 1:net[[2]]){
	  g.list[[l]] <- igraph::graph_from_adjacency_matrix(NodesTensor[[l]], 
	  	weighted = T, mode ="directed")
  }
  	return(g.list)
}

# Auxiliary, copied code for multiplex 3D plot with bugfixes
plot_multiplex3D_fix <-
  function(g.list,
           layer.colors,
           as.undirected = T,
           layer.layout = "auto",
           layer.labels = "auto",
           layer.labels.cex = 0.5,
           edge.colors = "#ffffff",
           edge.normalize = F,
           edge.size.scale = 1,
           node.colors = "#ffffff",
           node.size.values = 5,
           node.size.scale = 1,
           node.alpha = 1,
           edge.alpha = 1,
           layer.alpha = "auto",
           layout = "fr",
           show.nodeLabels = F,
           show.aggregate = F,
           aggr.alpha = "auto",
           aggr.color = "#dadada",
           node.colors.aggr = "#dadada",
           layer.scale = 2,
           layer.shift.x = 0,
           layer.shift.y = 0,
           layer.space = 3.5,
           FOV = 30) {
    # Generate a 3D visualization of the multiplex network
    
    # Arguments can be either "auto" or NA in most cases
    
    #If node.colors is a matrix Nodes x Layers, the color of each node can be assigned
    #If node.size.scale is a vector of size Layers, each layer will be scaled independently
    #If edge.size.scale is a vector of size Layers, each layer will be scaled independently
    #If show.aggregate is true, then node.colors.aggr could be set as well
    
    
    mypal <- layer.colors
    
    Layers <- length(g.list)
    Nodes <- igraph::vcount(g.list[[1]])
    
    if (!is.matrix(layer.layout) && layer.layout == "auto") {
      lay <-
        layoutMultiplex(g.list,
                        layout = layout,
                        ggplot.format = F,
                        box = T)
    } else {
      lay <- layer.layout
    }
    
    if (layer.alpha == "auto") {
      layer.alpha <- rep(0.5, Layers)
    }
    if (is.na(layer.labels) || is.null(layer.labels)) {
      layer.labels <- NA
    } else {
      if (layer.labels == "auto" || length(layer.labels) != Layers) {
        layer.labels <- paste("Layer", 1:Layers)
      }
      if (show.aggregate) {
        layer.labels <- c(layer.labels, "Aggregate")
      }
    }
    
    if (length(node.size.scale) == 1) {
      node.size.scale <- rep(node.size.scale, Layers)
    }
    
    if (length(edge.size.scale) == 1) {
      edge.size.scale <- rep(edge.size.scale, Layers)
    }
    
    LAYER_SCALE <- layer.scale
    LAYER_SHIFT_X <- layer.shift.x
    LAYER_SHIFT_Y <- layer.shift.y
    LAYER_SPACE <- layer.space
    
    PLOT_FOV <- FOV
    d <- 0
    
    bg3d(col = "white")
    
    for (l in 1:Layers) {
      if (as.undirected) {
        g.list[[l]] <- igraph::as.undirected(g.list[[l]])
      }
      
      if (node.size.values == "auto") {
        igraph::V(g.list[[l]])$size <-
          3 * node.size.scale[l] * sqrt(igraph::strength(g.list[[l]]))
      } else {
        igraph::V(g.list[[l]])$size <- node.size.values * node.size.scale[l]
      }
      
      if (!is.matrix(node.colors)) {
        if (node.colors == "auto") {
          node.col <- layer.colors[l]
        } else {
          node.col <- node.colors
        }
        igraph::V(g.list[[l]])$color <- node.col
      } else {
        igraph::V(g.list[[l]])$color <- node.colors[, l]
      }
      
      if (show.nodeLabels) {
        igraph::V(g.list[[l]])$label <- 1:igraph::gorder(g.list[[l]])
      } else {
        igraph::V(g.list[[l]])$label <- NA
      }
      
      if (edge.colors == "auto") {
        edge.col <- layer.colors[l]
      } else {
        edge.col <- edge.colors
      }
      igraph::E(g.list[[l]])$color <- edge.col
      
      if (!is.null(igraph::E(g.list[[l]])$weight)) {
        igraph::E(g.list[[l]])$width <- igraph::E(g.list[[l]])$weight
      } else {
        igraph::E(g.list[[l]])$width <- 1
      }
      
      if (edge.normalize) {
        igraph::E(g.list[[l]])$width <-
          edge.size.scale[l] * log(1 + igraph::E(g.list[[l]])$width) / max(log(1 + igraph::E(g.list[[l]])$width))
      }
      
      if (show.aggregate) {
        d <- -1 + LAYER_SCALE * LAYER_SPACE * l / (Layers + 1)
      } else {
        d <- -1 + LAYER_SCALE * LAYER_SPACE * l / Layers
      }
      #print(d)
      
      layout.layer <- matrix(0, nrow = Nodes, ncol = 3)
      layout.layer[, 1] <- lay[, 1] + (l - 1) * LAYER_SHIFT_X
      layout.layer[, 2] <- lay[, 2] + (l - 1) * LAYER_SHIFT_Y
      layout.layer[, 3] <- d
      
      x <-
        c(-1, -1, -1 + LAYER_SCALE, -1 + LAYER_SCALE) + (l - 1) * LAYER_SHIFT_X
      y <-
        c(-1 + LAYER_SCALE, -1, -1, -1 + LAYER_SCALE) + (l - 1) * LAYER_SHIFT_Y
      z <- c(d, d, d, d)
      quads3d(x,
              y,
              z,
              alpha = layer.alpha[[l]],
              col = layer.colors[[l]],
              add = T)
    
      igraph::rglplot(g.list[[l]], layout = layout.layer,
              rescale = F)
      
      
        text3d(
          -1 + (l - 1) * LAYER_SHIFT_X,
          -1 + (l - 1) * LAYER_SHIFT_Y,
          d + 0.1,
          text = layer.labels[l],
          adj = 0.2,
          color = "black",
          family = "sans",
          cex = layer.labels.cex
        )
      
    }
    
    if (show.aggregate) {
      g.aggr <- GetAggregateNetworkFromNetworkList(g.list)
      
      if (node.size.values == "auto") {
        igraph::V(g.aggr)$size <- 3 * node.size.scale[l] * sqrt(igraph::strength(g.aggr))
      } else {
        igraph::V(g.aggr)$size <- node.size.values * node.size.scale[l]
      }
      
      igraph::V(g.aggr)$color <- node.colors.aggr
      
      if (show.nodeLabels) {
        igraph::V(g.aggr)$label <- 1:igraph::gorder(g.aggr)
      } else {
        igraph::V(g.aggr)$label <- NA
      }
      
      igraph::E(g.aggr)$color <- aggr.color
      
      if (!is.null(igraph::E(g.aggr)$weight)) {
        igraph::E(g.aggr)$width <- igraph::E(g.aggr)$weight
      } else {
        igraph::E(g.aggr)$width <- 1
      }
      
      l <- Layers + 1
      d <- -1 + LAYER_SCALE * LAYER_SPACE * l / (Layers + 1)
      layout.layer <- matrix(0, nrow = Nodes, ncol = 3)
      layout.layer[, 1] <- lay[, 1] + (l - 1) * LAYER_SHIFT_X
      layout.layer[, 2] <- lay[, 2] + (l - 1) * LAYER_SHIFT_Y
      layout.layer[, 3] <- d
      
      x <-
        c(-1, -1, -1 + LAYER_SCALE, -1 + LAYER_SCALE) + (l - 1) * LAYER_SHIFT_X
      y <-
        c(-1 + LAYER_SCALE, -1, -1, -1 + LAYER_SCALE) + (l - 1) * LAYER_SHIFT_Y
      z <- c(d, d, d, d)
      
      if (aggr.alpha == "auto") {
        quads3d(x,
                y,
                z,
                alpha = 0.5,
                col = aggr.color,
                add = T)
      } else {
        quads3d(x,
                y,
                z,
                alpha = aggr.alpha,
                col = aggr.color,
                add = T)
      }
      
      igraph::rglplot(g.aggr, layout = layout.layer,
              rescale = F)
      
     
        text3d(
          -1 + (l - 1) * LAYER_SHIFT_X,
          -1 + (l - 1) * LAYER_SHIFT_Y,
          d + 0.1,
          text = "Aggregate",
          adj = 0.2,
          color = "black",
          family = "sans",
          cex = layer.labels.cex
        )
      
      
    }
    
    
    M <- matrix(0, ncol = 4, nrow = 4)
    M[1, ] <- c(0.54, 0, 0.84, 0)
    M[2, ] <- c(0.33, 0.92, -0.22, 0)
    M[3, ] <- c(-0.77, 0.39, 0.5, 0)
    M[4, ] <- c(0, 0, 0, 1)
    
    par3d(FOV = PLOT_FOV, userMatrix = M)
  }


# net<-load_net(c("../data/cs-aarhus/aucs.config"))
# netlist<-sam_to_netlist(net)

# plot_network(net,netlist)
# rgl.snapshot("aucs3.png",fmt="png")


