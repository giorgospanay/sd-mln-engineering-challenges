# Other imports
library(pryr)

# Loads a network from file and aggregates it into a monoplex.
# Time performance. Also, track memory consumption -- to be done manually??
exp1 <- function(filenames){
	# Load file. Track performance & memory consumption
	# --------------------------
	trace_load_curr <- mem_change({
		time_load_s <- Sys.time()
		net <- load_net(filenames)
		time_load_e <- Sys.time()
		time_load_t <- time_load_e-time_load_s
	})
	# --------------------------

  	# Aggregate net. Track performance & memory consumption
	# --------------------------
	trace_aggr_curr <- mem_change({
		time_aggr_s <- Sys.time()
		net_aggr <- aggregate(net)
		time_aggr_e <- Sys.time()
		time_aggr_t <- time_aggr_e-time_aggr_s
	})
	# --------------------------
	

  	cat(sprintf("Loading time (in sec.): %f\n",time_load_t))
  	cat(sprintf("Loading mem curr (in bytes): %d\n",trace_load_curr))
  	cat(sprintf("Aggregate time (in sec.): %f\n",time_aggr_t))
  	cat(sprintf("Aggregate mem curr (in bytes): %d\n",trace_aggr_curr))

  	return(net_aggr)
}

# Loads a network from file and gets degrees for all nodes.
exp2 <- function(filenames){
	# Load file. Track performance & memory consumption
	# --------------------------
	trace_load_curr <- mem_change({
		time_load_s <- Sys.time()
		net <- load_net(filenames)
		time_load_e <- Sys.time()
		time_load_t <- time_load_e-time_load_s
	})
	# --------------------------

  	# Calculate degrees. Track performance & memory consumption
	# --------------------------
	trace_degs_curr <- mem_change({
		time_degs_s <- Sys.time()
		degs <- get_degree(net)
		time_degs_e <- Sys.time()
		time_degs_t <- time_degs_e-time_degs_s
	})
	# --------------------------
	

  	cat(sprintf("Loading time (in sec.): %f\n",time_load_t))
  	cat(sprintf("Loading mem curr (in bytes): %d\n",trace_load_curr))
  	cat(sprintf("Degree time (in sec.): %f\n",time_degs_t))
  	cat(sprintf("Degree mem curr (in bytes): %d\n",trace_degs_curr))

  	return(degs)
}

# Loads a network from file and runs InfoMap.
exp3 <- function(filenames){
	# Load file. Track performance & memory consumption
	# --------------------------
	trace_load_curr <- mem_change({
		time_load_s <- Sys.time()
		net <- load_net(filenames)
		time_load_e <- Sys.time()
		time_load_t <- time_load_e-time_load_s
	})
	# --------------------------

  	# Run InfoMap. Track performance & memory consumption
	# --------------------------
	trace_cdet_curr <- mem_change({
		time_cdet_s <- Sys.time()
		comms <- run_infomap(net)
		time_cdet_e <- Sys.time()
		time_cdet_t <- time_cdet_e-time_cdet_s
	})
	# --------------------------
	

  	cat(sprintf("Loading time (in sec.): %f\n",time_load_t))
  	cat(sprintf("Loading mem curr (in bytes): %d\n",trace_load_curr))
  	cat(sprintf("InfoMap time (in sec.): %f\n",time_cdet_t))
  	cat(sprintf("InfoMap mem curr (in bytes): %d\n",trace_cdet_curr))

  	return(comms)
}

# Generates a multiplex network and aggregates it into a monoplex.
# Time performance. Also, track memory consumption -- to be done manually??
exp4 <- function(n,l){
	# Generate net. Track performance & memory consumption
	# --------------------------
	trace_gens_curr <- mem_change({
		time_gens_s <- Sys.time()
		net <- gen_network(n,l)
		time_gens_e <- Sys.time()
		time_gens_t <- time_gens_e-time_gens_s
	})
	# --------------------------

  	# Aggregate net. Track performance & memory consumption
	# --------------------------
	trace_aggr_curr <- mem_change({
		time_aggr_s <- Sys.time()
		net_aggr <- aggregate(net)
		time_aggr_e <- Sys.time()
		time_aggr_t <- time_aggr_e-time_aggr_s
	})
	# --------------------------
	

  	cat(sprintf("Generate time (in sec.): %f\n",time_gens_t))
  	cat(sprintf("Generate mem curr (in bytes): %d\n",trace_gens_curr))
  	cat(sprintf("Aggregate time (in sec.): %f\n",time_aggr_t))
  	cat(sprintf("Aggregate mem curr (in bytes): %d\n",trace_aggr_curr))

  	return(net_aggr)
}

# Generates a multiplex network and gets degrees for all nodes.
exp5 <- function(n,l){
	#  Generate net. Track performance & memory consumption
	# --------------------------
	trace_gens_curr <- mem_change({
		time_gens_s <- Sys.time()
		net <- gen_network(n,l)
		time_gens_e <- Sys.time()
		time_gens_t <- time_gens_e-time_gens_s
	})
	# --------------------------

  	# Calculate degrees. Track performance & memory consumption
	# --------------------------
	trace_degs_curr <- mem_change({
		time_degs_s <- Sys.time()
		degs <- get_degree(net)
		time_degs_e <- Sys.time()
		time_degs_t <- time_degs_e-time_degs_s
	})
	# --------------------------
	

  	ccat(sprintf("Generate time (in sec.): %f\n",time_gens_t))
  	cat(sprintf("Generate mem curr (in bytes): %d\n",trace_gens_curr))
  	cat(sprintf("Degree time (in sec.): %f\n",time_degs_t))
  	cat(sprintf("Degree mem curr (in bytes): %d\n",trace_degs_curr))

  	return(degs)
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
#			aucs, fftw, citation, ff}
#		size -- Only applicable for synth; the size (in nodes) of the dataset. 
#			Options for now: {100,200,500,1000,2000,5000,10000,20000,50000}
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


	if (e_id<4){
		### DATASET IMPORTS ###
		#
		# Note: filenames should be in a format that the load/build... functions
		#		can process. Define new code for lib_input_type if necessary.
		#

		# Load synthetic multilayer network data. Expect second argument N (size)
		if (file=="synth"){
			filenames<-c("")
		}
		# Load London transport data (london-transport)
		else if (file=="london"){
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
		# Should not reach here. Add more cases for datasets above.
		else{
			stop("Dataset not found. See available arguments")
		}
	}
	# For generation experiments: retrieve tokens n-l
	else{
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