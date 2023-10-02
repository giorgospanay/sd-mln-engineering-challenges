
# Loads a network from file and aggregates it into a monoplex.
# Time performance. Also, track memory consumption -- to be done manually??
exp1 <- function(filenames){
	time_load_s <- Sys.time()
	# --------------------------
	net <- load_net(filenames)
	# --------------------------
  	time_load_e <- Sys.time()
  	time_load_t <- time_load_e-time_load_s


  	time_aggr_s <- Sys.time()
	# --------------------------
	net_aggr <- aggregate(net)
	# --------------------------
  	time_aggr_e <- Sys.time()
  	time_aggr_t <- time_aggr_e-time_aggr_s

  	cat(sprintf("Loading time: %f\n",time_load_t))
  	cat(sprintf("Aggregate time: %f\n",time_aggr_t))
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
	#

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
	# mully import
	else if (lib=="mully"){
		lib_util_path <- "mully-util.R"
		# TODO: fix
		lib_input_type <- 0
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
			filenames<-c("../data/london-transport/")
		}
		else if (lib_input_type==2){
			filenames<-c("../data/london-transport/london_transport_nodes.txt","../data/london-transport/london_transport_multiplex.edges","../data/london-transport/london_transport_layers.txt")
		}
		else if (lib_input_type==3){
			filenames<-c("../data/london-transport/london.config")
		}
	}
	# Load EUAir transport data (euair-transport)
	else if (file=="euair"){
		if (lib_input_type==1){
			filenames<-c("../data/euair-transport/")
		}
		else if (lib_input_type==2){
			filenames<-c("../data/euair-transport/EUAirTransportation_nodes.txt","../data/euair-transport/EUAirTransportation_multiplex.edges","../data/euair-transport/EUAirTransportation_layers.txt")
		}
		else if (lib_input_type==3){
			filenames<-c("../data/euair-transport/euair.config")
		}
	}
	# Load CS@Aarhus data (cs-aarhus)
	else if (file=="aucs"){
		if (lib_input_type==1){
			filenames<-c("../data/cs-aarhus/aucs.mpx")
		}
		else if (lib_input_type==2){	
			filenames<-c("../data/cs-aarhus/CS-Aarhus_nodes.txt","cs-aarhus/CS-Aarhus_multiplex.edges","cs-aarhus/CS-Aarhus_layers.txt")
		}
		else if (lib_input_type==3){
			filenames<-c("../data/cs-aarhus/aucs.config")
		}
	}
	# Load FriendFeed-Twitter data (ff-tw)
	else if (file=="fftw"){
		if (lib_input_type==1){
			filenames<-c("../data/ff-tw/fftw.mpx")
		}
		else if (lib_input_type==2){
			filenames<-c("")
		}	
		else if (lib_input_type==3){
			filenames<-c("")
		}
	}
	# Load citation data (journal-citation)
	else if (file=="citation"){
		filenames<-c("")
	}
	# Load FriendFeed data (friendfeed)
	else if (file=="ff"){
		filenames<-c("")
	}
	# Should not reach here. Add more cases for datasets above.
	else{
		stop("Dataset not found. See available arguments")
	}


	### EXPERIMENTS ###

	#Print exp, lib, file stats and call exp# which prints the rest.
	cat(sprintf("Exp%d: lib=%s, file=%s\n",e_id,lib,file))
	# Experiment 1: Load net from file & aggregate
	if (e_id==1){
		exp1(filenames)
	} 
	# Experiment 2:
	else if (e_id==2){

	}
	# ...
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