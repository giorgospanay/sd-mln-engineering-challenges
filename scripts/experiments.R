# Other imports
#library(pryr)
library(hash)

# Loads a network from file and aggregates it into a monoplex.
# Time performance. Also, track memory consumption -- to be done manually??
exp1 <- function(filenames){
	# Load file. Track performance & memory consumption
	# # --------------------------
	# trace_load_curr <- mem_change({
	# 	time_load_s <- proc.time()
	# 	net <- load_net(filenames)
	# 	time_load_e <- proc.time()
	# 	time_load_t <- time_load_e-time_load_s
	# })
	# # --------------------------
	# --------------------------
	time_load_s <- proc.time()
	net <- load_net(filenames)
	time_load_e <- proc.time()
	time_load_t <- time_load_e-time_load_s
	# --------------------------

  	# Aggregate net. Track performance & memory consumption
	# # --------------------------
	# trace_aggr_curr <- mem_change({
	# 	time_aggr_s <- proc.time()
	# 	net_aggr <- aggregate(net)
	# 	time_aggr_e <- proc.time()
	# 	time_aggr_t <- time_aggr_e-time_aggr_s
	# })
	# # --------------------------
	# --------------------------
	time_aggr_s <- proc.time()
	net_aggr <- aggregate(net)
	time_aggr_e <- proc.time()
	time_aggr_t <- time_aggr_e-time_aggr_s

  	cat(sprintf("Loading time (in sec.): %f\n",time_load_t[[3]]))
  	#cat(sprintf("Loading mem curr (in bytes): %d\n",trace_load_curr))
  	cat(sprintf("Aggregate time (in sec.): %f\n",time_aggr_t[[3]]))
  	#cat(sprintf("Aggregate mem curr (in bytes): %d\n",trace_aggr_curr))

  	return(net_aggr)
}

# Loads a network from file and gets degrees for all nodes.
exp2 <- function(filenames){
	# Load file. Track performance & memory consumption
	# # --------------------------
	# trace_load_curr <- mem_change({
	# 	time_load_s <- proc.time()
	# 	net <- load_net(filenames)
	# 	time_load_e <- proc.time()
	# 	time_load_t <- time_load_e-time_load_s
	# })
	# # --------------------------
	time_load_s <- proc.time()
	net <- load_net(filenames)
	time_load_e <- proc.time()
	time_load_t <- time_load_e-time_load_s

  	# Calculate degrees. Track performance & memory consumption
	# # --------------------------
	# trace_degs_curr <- mem_change({
	# 	time_degs_s <- proc.time()
	# 	degs <- get_degree(net)
	# 	time_degs_e <- proc.time()
	# 	time_degs_t <- time_degs_e-time_degs_s
	# })
	# # --------------------------
	
	time_degs_s <- proc.time()
	degs <- get_degree(net)
	time_degs_e <- proc.time()
	time_degs_t <- time_degs_e-time_degs_s

  	cat(sprintf("Loading time (in sec.): %f\n",time_load_t[[3]]))
  	#cat(sprintf("Loading mem curr (in bytes): %d\n",trace_load_curr))
  	cat(sprintf("Degree time (in sec.): %f\n",time_degs_t[[3]]))
  	#cat(sprintf("Degree mem curr (in bytes): %d\n",trace_degs_curr))

  	return(degs)
}

# Loads a network from file and runs InfoMap.
exp3 <- function(filenames){
	# Load file. Track performance & memory consumption
	# # --------------------------
	# trace_load_curr <- mem_change({
	# 	time_load_s <- proc.time()
	# 	net <- load_net(filenames)
	# 	time_load_e <- proc.time()
	# 	time_load_t <- time_load_e-time_load_s
	# })
	# # --------------------------
	time_load_s <- proc.time()
	net <- load_net(filenames)
	time_load_e <- proc.time()
	time_load_t <- time_load_e-time_load_s

  	# Run InfoMap. Track performance & memory consumption
	# # --------------------------
	# trace_cdet_curr <- mem_change({
	# 	time_cdet_s <- proc.time()
	# 	comms <- run_infomap(net)
	# 	time_cdet_e <- proc.time()
	# 	time_cdet_t <- time_cdet_e-time_cdet_s
	# })
	# # --------------------------
	time_cdet_s <- proc.time()
	comms <- run_infomap(net)
	time_cdet_e <- proc.time()
	time_cdet_t <- time_cdet_e-time_cdet_s

  	cat(sprintf("Loading time (in sec.): %f\n",time_load_t[[3]]))
  	#cat(sprintf("Loading mem curr (in bytes): %d\n",trace_load_curr))
  	cat(sprintf("InfoMap time (in sec.): %f\n",time_cdet_t[[3]]))
  	#cat(sprintf("InfoMap mem curr (in bytes): %d\n",trace_cdet_curr))

  	return(comms)
}

# Generates a multiplex network and aggregates it into a monoplex.
# Time performance. Also, track memory consumption -- to be done manually??
exp4 <- function(n,l){
	# Generate net. Track performance & memory consumption
	# # --------------------------
	# trace_gens_curr <- mem_change({
	# 	time_gens_s <- proc.time()
	# 	net <- gen_network(n,l)
	# 	time_gens_e <- proc.time()
	# 	time_gens_t <- time_gens_e-time_gens_s
	# })
	# # --------------------------
	time_gens_s <- proc.time()
	net <- gen_network(n,l)
	time_gens_e <- proc.time()
	time_gens_t <- time_gens_e-time_gens_s

  	# Aggregate net. Track performance & memory consumption
	# # --------------------------
	# trace_aggr_curr <- mem_change({
	# 	time_aggr_s <- proc.time()
	# 	net_aggr <- aggregate(net)
	# 	time_aggr_e <- proc.time()
	# 	time_aggr_t <- time_aggr_e-time_aggr_s
	# })
	# # --------------------------
	time_aggr_s <- proc.time()
	net_aggr <- aggregate(net)
	time_aggr_e <- proc.time()
	time_aggr_t <- time_aggr_e-time_aggr_s

  	cat(sprintf("Generate time (in sec.): %f\n",time_gens_t[[3]]))
  	#cat(sprintf("Generate mem curr (in bytes): %d\n",trace_gens_curr))
  	cat(sprintf("Aggregate time (in sec.): %f\n",time_aggr_t[[3]]))
  	#cat(sprintf("Aggregate mem curr (in bytes): %d\n",trace_aggr_curr))

  	return(net_aggr)
}

# Generates a multiplex network and gets degrees for all nodes.
exp5 <- function(n,l){
	#  Generate net. Track performance & memory consumption
	# # --------------------------
	# trace_gens_curr <- mem_change({
	# 	time_gens_s <- proc.time()
	# 	net <- gen_network(n,l)
	# 	time_gens_e <- proc.time()
	# 	time_gens_t <- time_gens_e-time_gens_s
	# })
	# # --------------------------
	time_gens_s <- proc.time()
	net <- gen_network(n,l)
	time_gens_e <- proc.time()
	time_gens_t <- time_gens_e-time_gens_s

  	# Calculate degrees. Track performance & memory consumption
	# # --------------------------
	# trace_degs_curr <- mem_change({
	# 	time_degs_s <- proc.time()
	# 	degs <- get_degree(net)
	# 	time_degs_e <- proc.time()
	# 	time_degs_t <- time_degs_e-time_degs_s
	# })
	# # --------------------------
	time_degs_s <- proc.time()
	degs <- get_degree(net)
	time_degs_e <- proc.time()
	time_degs_t <- time_degs_e-time_degs_s

  	cat(sprintf("Generate time (in sec.): %f\n",time_gens_t[[3]]))
  	#cat(sprintf("Generate mem curr (in bytes): %d\n",trace_gens_curr))
  	cat(sprintf("Degree time (in sec.): %f\n",time_degs_t[[3]]))
  	#cat(sprintf("Degree mem curr (in bytes): %d\n",trace_degs_curr))

  	return(degs)
}

# Loads a generated multiplex network and aggregates the layers.
exp6 <- function(filenames){
	# Behaviour identical to exp1. Different experiment id for logging purposes.
	return (exp1(filenames))
}


# Loads a generated multiplex network and gets degrees for all nodes.
exp7 <- function(filenames){
	# Behaviour identical to exp2. Different experiment id for logging purposes.
	return (exp2(filenames))
}


# experiment 8: Read synth multiplex network (1000-0-10), then for each of S steps
# delete and create an edge
exp8 <- function(filenames, s) {
  edges <- hash()

  init_time <- c()
  rem_time <- c()
  add_time <- c()
  all_time<-c(0.0)

  # Graph init: read network (synth-empty/1000-0-10)
  #net <- load_net(filenames)
  net<-read_empty(filenames)

  # Set constants:
  NUM_NODES <- 1000
  NUM_LAYERS <- 10
  NUM_INIT<-10000


# Graph init steps (=E)
for (i in 1:NUM_INIT) {
  # Add random edge
  n1 <- sample(1:NUM_NODES, 1)
  n2 <- sample(1:NUM_NODES, 1)
  l <- sample(1:NUM_LAYERS, 1)
  
  if (!(as.character(n1) %in% keys(edges))) {
    edges[[as.character(n1)]] <- hash()
  }
  
  if (!(as.character(n2) %in% keys(edges[[as.character(n1)]]))) {
    edges[[as.character(n1)]][[as.character(n2)]] <- hash()
  }
  
  if (!(as.character(l) %in% keys(edges[[as.character(n1)]][[as.character(n2)]]))) {
    edges[[as.character(n1)]][[as.character(n2)]][[as.character(l)]] <- TRUE 

    time_add1_s <- Sys.time()
    # --- MODULE ADD CALL START ---
    net <- add_edge(net, n1, n2, l)
    # --- MODULE ADD CALL END ---
    time_add1_e <- Sys.time()
    time_add1_t <- as.numeric(difftime(time_add1_e, time_add1_s, units = "secs"))
    # Add to init_time list for plotting later
    init_time <- c(init_time, time_add1_t)
    all_time <- c(all_time, time_add1_t)
  }
}

# Graph evolution steps (=S)
for (i in 1:s) {
  # Delete random edge
  n1 <- as.character(sample(keys(edges), 1))
  n2 <- as.character(sample(keys(edges[[n1]]), 1))
  l <- as.character(sample(keys(edges[[n1]][[n2]]), 1))
  
  del(l,edges[[n1]][[n2]])
  
  if (length(keys(edges[[n1]][[n2]])) == 0) {
    edges[[n1]][[n2]] <- NULL
  }
  
  if (length(keys(edges[[n1]])) == 0) {
    edges[[n1]] <- NULL
  }

  time_remv_s <- Sys.time()
  # --- MODULE ADD CALL START ---
  net <- rem_edge(net, as.numeric(n1), as.numeric(n2), as.numeric(l))
  # --- MODULE ADD CALL END ---
  time_remv_e <- Sys.time()
  time_remv_t <- as.numeric(difftime(time_remv_e, time_remv_s, units = "secs"))
  # Add to rem_time list for plotting later
  rem_time <- c(rem_time, time_remv_t)
  all_time <- c(all_time, time_remv_t)

  # Add random edge
  n1 <- sample(1:NUM_NODES, 1)
  n2 <- sample(1:NUM_NODES, 1)
  l <- sample(1:NUM_LAYERS, 1)

  if (!(as.character(n1) %in% keys(edges))) {
    edges[[as.character(n1)]] <- hash()
  }
  
  if (!(as.character(n2) %in% keys(edges[[as.character(n1)]]))) {
    edges[[as.character(n1)]][[as.character(n2)]] <- hash()
  }
  
  if (!(as.character(l) %in% keys(edges[[as.character(n1)]][[as.character(n2)]]))) {
    edges[[as.character(n1)]][[as.character(n2)]][[as.character(l)]] <- TRUE

   time_add2_s <- Sys.time()
    # --- MODULE ADD CALL START ---
    net <- add_edge(net, n1, n2, l)
    # --- MODULE ADD CALL END ---
    time_add2_e <- Sys.time()
    time_add2_t <- as.numeric(difftime(time_add2_e, time_add2_s, units = "secs"))
    # Add to add_time list for plotting later
    add_time <- c(add_time, time_add2_t)
    all_time <- c(all_time, time_add2_t)
  }
}

  # Print times sum
  sum_time<-0.0
  for (t in all_time){
  	sum_time=sum_time+t
  	cat(sprintf("%f\n",sum_time))
  }

  cat(sprintf("-----------------\n"))

  return(edges)
}


# More experiments go here

# Chicken chow main. Set up so that the same main util template can be used
#   on all experiments; most of the changes need to be done on the load_net(), 
#   build(), aggregate(), ... methods. 
# 
# Expecting commandline arguments for script to run. 
# Example: Rscript experiments.R e_id lib file [size]
#	where:
#		e_id -- The experiment id to run. See details on function comments & paper.
#		lib  -- The Python library to use. Options now: {muxviz, multinet, mully} 
#		file -- The dataset to use. Options for now: {synth, london, euair, 
#			aucs, fftw, citation, ff}. Alternatively: code for synth/generated net.
#	
main <- function(){
	# Get arguments from command line. Only trailing arguments
	args <- commandArgs(trailingOnly=TRUE)
	if (length(args)<3){
		stop("Not enough arguments given. Usage: Rscript experiments.R exp_id library file [size]")
	}

	e_id <- strtoi(args[1])
	lib <- args[2]
	file <- args[3]
	n<-0
	l<-0
	e_g<-0
	e<-""

	### LIBRARY MODULE IMPORTS ###

	# Import library util sources. All source util files contain the functions 
	# 	necessary to run experiments.
	# In order to run similar experiments for a new library, one should create 
	#	the file (lib)-util.R with the necessary functions (see all other R
	#	utililty scripts listed here) and import the source code here.
	#
	# Also, here one should note the file input type for the library.
	# Available codes (feel free to define own if necessary):
	# 	1 -- multinet-native, one file for all
	#	2 -- Node/edge/layer files input
	#	3 -- MuxViz input, node/edge/layer-files coded in a semicolon-separated 
	#		config.file
	#	4 -- Custom file for netmem. First line: max_node_id, max_layer_id. Rest is
	#		normal multiplex edgelist file.

	lib_util_path <- ""
	lib_input_type <- 0

	# MuxViz import
	if (lib=="muxviz"){
		lib_util_path <- "muxviz-util.R"
		lib_input_type <- 3
	} 
	# multinet import
	else if (lib=="multinet"){
		lib_util_path <- "multinet-util.R"
		lib_input_type <- 1
	}
	# netmem import
	else if (lib=="netmem"){
		lib_util_path <- "netmem-util.R"
		lib_input_type <- 4
	}
	# ... other libs ...
	# Should not reach this statement
	else{
		stop("No library util file found for argument")
	}

	# Import defined functions from util file
	if(!exists("load_net", mode="function")) source(lib_util_path)
	if(!exists("aggregate", mode="function")) source(lib_util_path)
	# Add more here.

	# For file reading experiments:
	if (e_id<=3 || e_id>=6){
		### DATASET IMPORTS ###
		#
		# Note: filenames should be in a format that the load/build... functions
		#		can process. Define new code for lib_input_type if necessary.
		#
		# Load London transport data (london-transport)
		if (file=="london"){
			if (lib_input_type==1){
				filenames<-c("../data/london-transport/london.mpx")
				# filenames<-c("../data/london-transport/london-full.mpx")
			}
			else if (lib_input_type==2){
				filenames<-c("../data/london-transport/london_transport_nodes.txt","../data/london-transport/london_transport_multiplex.edges","../data/london-transport/london_transport_layers.txt")
			}
			else if (lib_input_type==3){
				filenames<-c("../data/london-transport/london.config")
			}
			else if (lib_input_type==4){
				filenames<-c("../data/london-transport/london_transport_netmem.edges")
			}
		}
		# Load EUAir transport data (euair-transport)
		else if (file=="euair"){
			if (lib_input_type==1){
				filenames<-c("../data/euair-transport/euair.mpx")
				# filenames<-c("../data/euair-transport/euair-full.mpx")
			}
			else if (lib_input_type==2){
				filenames<-c("../data/euair-transport/EUAirTransportation_nodes.txt","../data/euair-transport/EUAirTransportation_multiplex.edges","../data/euair-transport/EUAirTransportation_layers.txt")
			}
			else if (lib_input_type==3){
				filenames<-c("../data/euair-transport/euair.config")
			}
			else if (lib_input_type==4){
				filenames<-c("../data/euair-transport/EUAirTransportation_netmem.edges")
			}
		}
		# Load CS@Aarhus data (cs-aarhus)
		else if (file=="aucs"){
			if (lib_input_type==1){
				filenames<-c("../data/cs-aarhus/aucs.mpx")
			}
			else if (lib_input_type==2){	
				filenames<-c("../data/cs-aarhus/CS-Aarhus_nodes.txt","../data/cs-aarhus/CS-Aarhus_multiplex.edges","../data/cs-aarhus/CS-Aarhus_layers.txt")
			}
			else if (lib_input_type==3){
				filenames<-c("../data/cs-aarhus/aucs.config")
			}
			else if (lib_input_type==4){
				filenames<-c("../data/cs-aarhus/CS-Aarhus_netmem.edges")
			}

		}
		# Load FriendFeed-Twitter data (ff-tw)
		else if (file=="fftw"){
			if (lib_input_type==1){
				filenames<-c("../data/ff-tw/fftw.mpx")
			}
			else if (lib_input_type==2){
				filenames<-c("../data/ff-tw/fftw_nodes.txt","../data/ff-tw/fftw_multiplex.edges","../data/ff-tw/fftw_layers.txt")
			}	
			else if (lib_input_type==3){
				filenames<-c("../data/ff-tw/fftw.config")
			}
			else if (lib_input_type==4){
				filenames<-c("../data/ff-tw/fftw_netmem.edges")
			}

		}
		# Load FriendFeed data (friendfeed)
		else if (file=="ff"){
			if (lib_input_type==1){
				filenames<-c("../data/friendfeed/ff_simple.mpx")
			}
			else if (lib_input_type==2){
				filenames<-c("../data/friendfeed/friendfeed_nodes.txt","../data/friendfeed/friendfeed_multiplex.edges","../data/friendfeed/friendfeed_layers.txt")
			}	
			else if (lib_input_type==3){
				filenames<-c("../data/friendfeed/friendfeed.config")
			}
			else if (lib_input_type==4){
				filenames<-c("../data/friendfeed/friendfeed_netmem.edges")
			}
		}
		# Otherwise: synthetic data, coded as "n-e-l[+library extension]"
		else{
			if (lib_input_type==1){
				filenames<-c(paste("../data/synth/",file,".mpx",sep=""))
			}
			else if (lib_input_type==2){
				filenames<-c(paste("../data/synth/",file,"_nodes.txt",sep=""),paste("../data/synth/",file,".edges",sep=""),paste("../data/synth/",file,"_layers.txt",sep=""))
			}	
			else if (lib_input_type==3){
				filenames<-c(paste("../data/synth/",file,".config",sep=""))
			}
			else if (lib_input_type==4){
				filenames<-c(paste("../data/synth/",file,"_netmem.edges",sep=""))
			}
		}
	}
	# For generation experiments (4-5): retrieve tokens n-l
	else if (e_id==4 || e_id==5){
		toks<-strsplit(file,"-")
		n<-strtoi(toks[[1]][1])
		l<-strtoi(toks[[1]][2])
	}


	### EXPERIMENTS ###

	#Print exp, lib, file stats and call exp# which prints the rest.
	cat(sprintf("Exp%d: lib=%s, file=%s\n",e_id,lib,file))
	# Experiment 1: Load net from file & aggregate
	if (e_id==1){
		exp1(filenames)
	} 
	# Experiment 2: Load net from files & calculate degree 
	else if (e_id==2){
		exp2(filenames)
	} 
	# Experiment 3: Load net from file & run InfoMap
	else if (e_id==3){
		exp3(filenames)
	}
	# Experiment 4: Generate networks & aggregate
	else if (e_id==4){
		exp4(n,l)
	}
	# Experiment 5: Generate networks & calculate degrees
	else if (e_id==5){
		exp5(n,l)
	}
	# Experiment 6: Load net from synth & aggregate
	else if (e_id==6){
		exp6(filenames)
	}
	# Experiment 7: Load net from synth & calculate degree
	else if (e_id==7){
		exp7(filenames)
	}
	# Experiment 8: Load net from empty & rebuild random
	else if (e_id==8){
		exp8(filenames,10000)
	}
	#
	# ... Other experiments here ...
	#
	# Should not reach here
	else {
		stop("Experiment id not found. See comments/paper for available args")
	}
	cat(sprintf("-------------------------------\n"))

}

# To execute main.
if (!interactive()){
	main()
}