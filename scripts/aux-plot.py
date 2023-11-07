import parse
import pandas as pd
import numpy as np
import time
from matplotlib import pyplot as plt



def plot_exp1(library_colors):
    # Not used now, might be useful later.
    #pvt1=pd.pivot_table(df,columns="dataset",index="library")

    # Plot: bar chart, performance of network loading + aggregation for libraries.
    #    Different datasets. Two plots: one for smaller datasets, one for larger. 
    n_lib=len(library_colors)
    n_dset=len(datasets)
    r = np.arange(n_dset)
    width = 1.0/n_lib
    width_counter=0.0

    df_small = df[["dataset","library","load_time","aggr_time","total_time"]].loc[df["dataset"].isin(["aucs","london","euair"])].sort_values(["dataset","library"])
    



    print(df)
    print(df_small)

    # # Get small datasets plot
    # for d in ["aucs","london","euair"]:
    #   lib_c=0
    #   for l in ["multinet","muxviz","pymnet"]:
    #       m_found=df.loc[df["dataset"]==d]
    #       row_found=m_found.loc[m_found["library"]==l]
    #       print(row_found)
    #       plt.bar(r+width_counter,row_found["total_time"],color=library_colors[lib_c],width=width,edgecolor='black',label=l) 
    #       lib_c=lib_c+1
    #       width_counter=width_counter+width

    # plt.xlabel("Dataset") 
    # plt.ylabel("Execution time (sec.)") 
    # plt.title("Performance of network loading and layer aggregation") 
      
    # #plt.grid(linestyle='--') 
    # plt.xticks(r+width,["aucs","muxviz","pymnet"]) 
    # plt.legend() 
      
    # plt.show() 

    # Get large datasets plot

    df_large = df[["dataset","library","load_time","aggr_time","total_time"]].loc[df["dataset"].isin(["fftw","ff"])].sort_values(["dataset","library"])
    print(df_large)


def plot_exp4(file_a,file_b):
    # Read files
    df1=pd.read_csv(file_a,sep=" ",header=0)
    df1.replace(0,np.nan,inplace=True)
    df2=pd.read_csv(file_b,sep=" ",header=0)
    df2.replace(0,np.nan,inplace=True)

    # Plot: |L|=2, increasing node size
    fig1,ax1=plt.subplots()
    df1a=df1[["node_size","multinet_genr","muxviz_genr","pymnet_genr","py3plex_genr"]]
    df1a.plot(
        ax=ax1,
        x="node_size",
        logy=True,
        logx=True,
        xticks=df1["node_size"],
        style=['+--','o--','.:','x:'],
        title="Multiplex network generation time, increasing #vertices (|L|=2)"
    )
    ax1.legend(["multinet","MuxViz","Pymnet","Py3plex"])
    ax1.set_xlabel("Number of vertices")
    ax1.set_ylabel("Network generation time (sec.)")
    plt.show()

    # Plot: |V|=1000, increasing layer size
    fig2,ax2=plt.subplots()
    df2a=df2[["layer_size","multinet_genr","muxviz_genr","pymnet_genr","py3plex_genr"]]
    df2a.plot(
        ax=ax2,
        x="layer_size",
        logy=True,
        logx=True,
        xticks=df2["layer_size"],
        style=['+--','o--','.:','x:'],
        title="Multiplex network generation time, increasing #layers (|V|=1000)"
    )
    ax2.legend(["multinet","MuxViz","Pymnet","Py3plex"])
    ax2.set_xlabel("Number of layers")
    ax2.set_ylabel("Network generation time (sec.)")
    plt.show()

def plot_exp5(file_a,file_b):
    # Read files
    df1=pd.read_csv(file_a,sep=" ",header=0)
    df1.replace(0,np.nan,inplace=True)
    df2=pd.read_csv(file_b,sep=" ",header=0)
    df2.replace(0,np.nan,inplace=True)

    # Plot: |L|=2, increasing node size
    fig1,ax1=plt.subplots()
    df1a=df1[["node_size","multinet_genr","muxviz_genr","netmem_genr","pymnet_genr","py3plex_genr"]]
    df1a.plot(
        ax=ax1,
        x="node_size",
        logy=True,
        logx=True,
        xticks=df1["node_size"],
        style=['+--','o--','2--','.:','x:'],
        title="Multiplex network generation time, increasing #vertices (|L|=2)"
    )
    ax1.legend(["multinet","MuxViz","netmem","Pymnet","Py3plex"])
    ax1.set_xlabel("Number of vertices")
    ax1.set_ylabel("Network generation time (sec.)")
    plt.show()

    # Plot: |V|=1000, increasing layer size
    fig2,ax2=plt.subplots()
    df2a=df2[["layer_size","multinet_genr","muxviz_genr","netmem_genr","pymnet_genr","py3plex_genr"]]
    df2a.plot(
        ax=ax2,
        x="layer_size",
        logy=True,
        logx=True,
        xticks=df2["layer_size"],
        style=['+--','o--','2--','.:','x:'],
        title="Multiplex network generation time, increasing #layers (|V|=1000)"
    )
    ax2.legend(["multinet","MuxViz","netmem","Pymnet","Py3plex"])
    ax2.set_xlabel("Number of layers")
    ax2.set_ylabel("Network generation time (sec.)")
    plt.show()



# Mainest of the mains
def main():

    # # Run for experiment 4
    # plot_exp4("../logs/plot_exp4a.txt","../logs/plot_exp4b.txt")

    # Run for experiment 5
    plot_exp5("../logs/plot_exp5a.txt","../logs/plot_exp5b.txt")

    return

if __name__ == "__main__":
    main()
