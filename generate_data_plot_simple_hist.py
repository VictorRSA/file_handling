# #Author:Victor NKuna
# #Created:06-November-2020
# #Email:victor.nkuna
#
#
# from matplotlib import  pyplot as plt
# from matplotlib import colors
# from matplotlib.ticker import PercentFormatter
# import pandas as pd
#
# from random import*
# import numpy as np
#
# from scipy import*
# from matplotlib import cm
# from matplotlib.colors import ListedColormap, LinearSegmentedColormap
#
#
# N_points = 100000
# N_bins =20
#
# #generate a normal distribution and centre at x=0 y=5
#
# x=np.random.randn(N_points)
#
# y= 0.4*x+np.random.randn(N_points)+5
# fig,axes  =plt.subplots(1,2,sharey=True,tight_layout=True)
# # axes[0].hist(x,bins=20)
# # axes[1].hist(y,bins=20)
#
# # WE CAN SET THE NUMBER OF BINS WITH BBINS KWARG--KEY ARGUMENT
# #N is the count in each bin,bins is the lwoer-limit of the bin
#
# N,bins ,patches =axes[0].hist(x,bins=N_bins)
#
# #we will color code by the height,but one could uyse any scaller
#
# fracs = N/N.max()
#
# #we need to normalize the data to 0.1 for the full range of the colormap
#
# norm  =  colors.Normalize(fracs.min(),fracs.max())
# #we will now loop through our bjects and set the color of each accordingly
#
# for thisfrac,thispatch in zip(fracs,patches):
#     color_virdis = cm.get_cmap("viridis",12)
#     thispatch.set_facecolor(color_virdis)
# #we  can also normlaize our inputs by the total number of counts
#
# axes[1].hist(x,bins=N_bins,density=True)
# axes[1].yaxis.set_major_formatter(PercentFormatter(xmax=1))
#
# plt.show()
import numpy as n
import matplotlib.pyplot as plt

# Random gaussian data.
Ntotal = 1000
data = 0.05 * n.random.randn(Ntotal) + 0.5

# This is  the colormap I'd like to use.
cm = plt.cm.get_cmap('RdYlBu_r')

# Plot histogram.
n, bins, patches = plt.hist(data, 25, normed=1, color='green')
bin_centers = 0.5 * (bins[:-1] + bins[1:])

# scale values to interval [0,1]
col = bin_centers - min(bin_centers)
col /= max(col)

for c, p in zip(col, patches):
    plt.setp(p, 'facecolor', cm(c))

plt.show()
