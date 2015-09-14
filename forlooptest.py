#creating a for loop for normal vector

import yt
import matplotlib as plt
import numpy as np

def _Byz(field, data): #define a new field in y-z plane
 return np.sqrt(data["Y-magnfield"]**2+data["Z-magnfield"]**2)

fn="data.0510.3d.hdf5" 
ds=yt.load(fn) #load data
ds.periodicity=(True,True,True)
ds.add_field(("gas", "Byz"), function=_Byz, units="G", force_override=True)

L_list=[]

for x in range(1,3):
    for y in range(1,3):
          L=np.array([x,y,0])
          print L
          L_list.append(L)
            
print L_list
for i in L_list:
    oapp=yt.OffAxisProjectionPlot(ds, i, "Byz", weight_field="density")
    oapp.save("~/Documents/_NN_data/forlooptest/%s_oapp%s.png" % (fn, i))
