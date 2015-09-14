# Projected components of B-field as arrays

import yt 
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import AxesGrid
import numpy as np
import matplotlib.image as mpimg

#Project B-field in a plane - derive these

def _Bxy(field, data): #define a new field in x-y plane
	return np.sqrt(data["X-magnfield"]**2+data["Y-magnfield"]**2)

def _Byz(field, data): #define a new field in y-z plane
	return np.sqrt(data["Y-magnfield"]**2+data["Z-magnfield"]**2)
	
def _Bxz(field, data): #define a new field in x-z plane
	return np.sqrt(data["X-magnfield"]**2+data["Z-magnfield"]**2)

fn="data.0510.3d.hdf5" 
ds=yt.load(fn) #load dataset

#Make projection plots of the components of the field. Turn these into 2D arrays

mppx=yt.ProjectionPlot(ds, "z", "X-magnfield", weight_field="density") #Project X-component of B-field from z-direction
#mppx.save("projected-Bx.png") #save
imgx=mpimg.imread("projected-Bx.png") #imread turns an image into a 2D array
#print imgx

mppy=yt.ProjectionPlot(ds, "z", "Y-magnfield", weight_field="density") #Project Y-component of B-field from z-direction
#mppy.save("projected-By.png")
imgy=mpimg.imread("projected-By.png")
#print imgy

mppz=yt.ProjectionPlot(ds, "x", "Z-magnfield", weight_field="density")
#mppz.save("projected-Bz.png")
imgz=mpimg.imread("projected-Bz.png")
#print imgz

thetalist=[]
for i in range(len(imgx)):
    theta=np.arctan(imgx[i]/imgy[i])
    thetalist.append(theta)
print thetalist
