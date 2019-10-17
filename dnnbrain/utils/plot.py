# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 14:39:00 2019

@author: liuxingyu
"""

import matplotlib.pyplot as plt
import numpy as np

def imgarray_show(x, nrows=1, ncols=1, row_label=None, vmin=None, vmax=None,
               figsize=[10, 6], cmap='coolwarm', frame_on=True,
               show=True, save_path=None):
    """
    create a figure showing multiple images.
    
    Parameters
    ----------
    x[list]: list of image array (2d or 3d-RGB[A])
    nrows, ncols[int]: number of rows/columns of the subplot grid
    row_label[list]: lsit of str 
    vmin, vmax[scalar]: vmin and vmax define the data range 
        that the colormap covers. By default, the colormap covers 
        the complete value range of the supplied data. 
    figsize[float, float]: width, height of figure in inches.
    cmap[str]: The Colormap instance or registered colormap name used 
        to map scalar data to colors. 
    frame_on[bool]: set whether the axes rectangle patch is drawn
    show[bool]: set whether the figure is displayed
    
    """

    fig, axs = plt.subplots(nrows=nrows, ncols=ncols,
                            subplot_kw={'xticks': [], 'yticks': [],
                                        'frame_on': frame_on},
                            figsize=figsize)

    for i, ax in enumerate(axs.flat[:len(x)]):
        if np.mod(i, ncols) == 0:
            ax.set_ylabel(row_label[i//ncols])
        ax.imshow(x[i], cmap=cmap, vmin=vmin, vmax=vmax)

    plt.tight_layout()
    if show is True:
        plt.show()
    
    if save_path is not None:
        plt.savefig(save_path)
        