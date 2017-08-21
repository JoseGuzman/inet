"""
plots.py

Jose Guzman, sjm.guzman@gmail.com
Claudia Espinoza, claudia.espinoza@ist.ac.at

Created: Tue Aug 15 01:48:09 CEST 2017

Function to perform basic plotting.

Usage
-----

>>> from iplots import bar_plot
>>> from matplotib.pyplot import figure, show
>>> fig = figure()
>>> ax = fig.add_subplot(111)
>>> barplot(simulation, n_found)
>>> ax.set_title('My figure')
"""

import numpy as np
import matplotlib.pyplot as plt

def barplot(simulation, n_found, ax=None):
    """
    Plots a bar of simulated values versus the counts of
    the connections found experimentally and provide a P-Value
    for the null-hypothesis.

    Arguments
    ---------
    
    simulation : list
        a list containing the successes according to the null-hypothese.

    n_found: int
        the number of successes found empirically

    ax : plt.axis
        an axis object to plot it

    Returns
    -------

    an axis object with a bar plot together with standard deviation and
    P-values.
    """
    
    sim = np.array(simulation)
    p_val = len(sim[sim>n_found]) / float(sim.size)

    if ax is None:
        ax = plt.gca() # gets current axis if necessary

    x_pos = (0, 0.4) 
    x_labels = ('Simulation', 'Observation')

    # bar with SD
    ax.bar(x_pos, [sim.mean(), n_found],  \
        color = ('brown', 'white'), width =0.30, align='center', 
        edgecolor='black', linewidth =2, zorder = 2)
    ax.errorbar(x_pos, [sim.mean(), n_found], fmt=' ',\
        yerr=[sim.std(), 0], color='brown', capsize=12, 
        capthick = 3, elinewidth = 3, zorder = 1)
    ax.text(0.4, n_found + n_found*0.2,  'P = %2.4f'%p_val,\
        verticalalignment='center', horizontalalignment='center')

    # remove top and righ axis
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    ax.xaxis.set_ticks_position('none') # remove ticks in bottom spine

    # labels
    ax.set_xticks(x_pos)
    ax.set_xticklabels(x_labels) 
    ax.set_ylabel('Number of motifs')

    # remove grid just in case
    ax.grid(False)

    # axis limits
    mymax = max(sim.mean(), n_found)
    mymax += mymax*0.2 
    ax.set_ylim(ymax = mymax)

    return( ax )

def boxplot(mylist, ax = None):
    """
    Plots a box plot from a list of values.

    Arguments
    ---------
    
    mylist  : list
        A list containing the single data points to be plotted
    
    ax  : plt.axis
        an axis object to plot it
    
    """
    data = np.array(mylist)

    if ax is None:
        ax = plt.gca() # gets current axis if necessary
        
    xvalues = np.random.uniform(low =0.4, high = 0.60, size= data.size)

    # plot single data points
    ax.plot(xvalues, data, 'o', color = 'gray', ms = 8) # single datapoits
    
    # boxplot details
    boxplot = ax.boxplot(data, widths = .4, positions = [0.5], patch_artist = 1)
    
    for box in boxplot['boxes']: 
        box.set( color = 'white') # outline color
        box.set( edgecolor = 'black', linewidth = 3)
    for cap in boxplot['caps']:
        cap.set(color = 'black', linewidth = 3)
    for whisker in boxplot['whiskers']:
        whisker.set(color = 'black', linewidth = 3) # color/width 
        whisker.set(linestyle = '-') # continous line
    for median in boxplot['medians']:
        median.set(color = 'brown', linewidth = 4)

    # remove spines
    ax.get_xaxis().set_visible(0)
    ax.get_yaxis().tick_left()
    for sp in ['top', 'bottom', 'right']:
        ax.spines[sp].set_visible(0)
    
    return( ax )

if __name__ == '__main__':
    # some tests
    from matplotlib.pyplot import figure, show
    fig = figure()
    ax = fig.add_subplot(111)
    ax = boxplot(range(10))
    ax.set_ylim(-0.5,10)

    show()
    