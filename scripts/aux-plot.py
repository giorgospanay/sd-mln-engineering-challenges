import parse
import pandas as pd
import numpy as np
import time
from matplotlib import pyplot as plt


## Auxiliary plot functions ##
# Credit to pascscha for this: https://stackoverflow.com/questions/14270391/how-to-plot-multiple-bars-grouped
def bar_plot(ax, data, colors=None, total_width=0.8, single_width=1, legend=True):
    """Draws a bar plot with multiple bars per data point.

    Parameters
    ----------
    ax : matplotlib.pyplot.axis
        The axis we want to draw our plot on.

    data: dictionary
        A dictionary containing the data we want to plot. Keys are the names of the
        data, the items is a list of the values.

        Example:
        data = {
            "x":[1,2,3],
            "y":[1,2,3],
            "z":[1,2,3],
        }

    colors : array-like, optional
        A list of colors which are used for the bars. If None, the colors
        will be the standard matplotlib color cyle. (default: None)

    total_width : float, optional, default: 0.8
        The width of a bar group. 0.8 means that 80% of the x-axis is covered
        by bars and 20% will be spaces between the bars.

    single_width: float, optional, default: 1
        The relative width of a single bar within a group. 1 means the bars
        will touch eachother within a group, values less than 1 will make
        these bars thinner.

    legend: bool, optional, default: True
        If this is set to true, a legend will be added to the axis.
    """

    # Check if colors where provided, otherwhise use the default color cycle
    if colors is None:
        colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

    # Number of bars per group
    n_bars = len(data)

    # The width of a single bar
    bar_width = total_width / n_bars

    # List containing handles for the drawn bars, used for the legend
    bars = []

    # Iterate over all data
    for i, (name, values) in enumerate(data.items()):
        # The offset in x direction of that bar
        x_offset = (i - n_bars / 2) * bar_width + bar_width / 2

        # Draw a bar for every value of that type
        for x, y in enumerate(values):
            bar = ax.bar(x + x_offset, y, width=bar_width * single_width, color=colors[i % len(colors)])

        # Add a handle to the last drawn bar, which we'll need for the legend
        bars.append(bar[0])

    # Draw legend if we need
    if legend:
        ax.legend(bars, data.keys())


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



# if __name__ == "__main__":
#     # Usage example:
#     data = {
#         "a": [1, 2, 3, 2, 1],
#         "b": [2, 3, 4, 3, 1],
#         "c": [3, 2, 1, 4, 2],
#         "d": [5, 9, 2, 1, 8],
#         "e": [1, 3, 2, 2, 3],
#         "f": [4, 3, 1, 1, 4],
#     }

#     fig, ax = plt.subplots()
#     bar_plot(ax, data, total_width=.8, single_width=.9)
#     plt.show()
