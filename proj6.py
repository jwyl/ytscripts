#Plotting 6 on axis projections - the xy, yz, and xz planes from both directons

##Define a new field - projected magnetic field, for example in the y-z plane (x-direction).. Use simple derived fields in the yt cookbook.

import yt 
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import AxesGrid
import numpy as np

def _Bxy(field, data): #define a new field in x-y plane
	return np.sqrt(data["X-magnfield"]**2+data["Y-magnfield"]**2)

def _Byz(field, data): #define a new field in y-z plane
	return np.sqrt(data["Y-magnfield"]**2+data["Z-magnfield"]**2)
	
def _Bxz(field, data): #define a new field in x-z plane
	return np.sqrt(data["X-magnfield"]**2+data["Z-magnfield"]**2)
	
fn="data.0510.3d.hdf5" 
ds=yt.load(fn) #load dataset

ds.add_field(("gas", "Bxy"), function=_Bxy, units="G", force_override=True) #add the new field
ds.add_field(("gas", "Byz"), function=_Byz, units="G", force_override=True)
ds.add_field(("gas", "Bxz"), function=_Bxz, units="G", force_override=True)

fields = ["'gas', 'Bxy'"]

q=[1,-1]
L=(i,j,k)
L1list=L2list=L3list=[]
for x in enumerate (q):
    L1=(i,0,0)
    L2=(0,i,0)
    L3=(0,0,i)
    L1list.append(L1)
    L2list.append(L2)
    L3list.append(L3)
    print L1list
    for i, L3 in enumerate (L3list):
        oapp=yt.OffAxisProjectionPlot(ds, i, 'Bxy', weight_field="density")
        #plot=oapp.plots[i]
        #plot.figure=fig
        #images = plot.axes.images
        #plot.axes = grid[i].axes
        #plot.axes.images = images
        #plot.cax = grid.cbar_axes[i]
        #oapp.annotate_contour(("gas", "density"), ncont=5, factor=4)
        #oapp._setup_plots()
        #oapp.run_callbacks()
        
#plt.savefig("Bxy-z.png")
