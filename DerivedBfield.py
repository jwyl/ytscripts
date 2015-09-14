##Define a new field - projected magnetic field, for example in the y-z plane (x-direction).. Use simple derived fields in the yt cookbook.

import yt 
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import AxesGrid
import numpy as np
import matplotlib.image as mpimg

def _Byz(field, data): #define a new field in y-z plane
	return np.sqrt(data["Y-magnfield"]**2+data["Z-magnfield"]**2)
    
##For Bxy and Bxz, use the same form as for definition for _Byz 

fn="data.0510.3d.hdf5" 
ds=yt.load(fn) #load data
ds.periodicity=(True,True,True)
ds.add_field(("gas", "Byz"), function=_Byz, units="G", force_override=True)

#fig=plt.figure()

ad=ds.all_data()
#field = ["Byz"]
#p=yt.ProjectionPlot(ds, "x", field, weight_field="density")
#p.zoom(1)
#p.annotate_contour("Byz")
#p.annotate_magnetic_field()
#get(annotate_timestamp)
#p.run_callbacks()
#p.save()

L=np.array([2,1,1])
oap=yt.off_axis_projection(ds, ds.domain_center, L, ds.domain_width, (800, 800), "density")
#yt.write_oap()

oapp=yt.OffAxisProjectionPlot(ds, L, "Byz", weight_field="density")
oapp.annotate_contour(("gas", "density"), ncont=5, factor=4)
#oapp.annotate_magnetic_field()
#oapp.save('contours+vectors_density')
#oapp.save() #to save and include name use oapp.save("%s_oapp.png" % ds)

prj=ds.proj("Byz", "x", weight_field="density")
print prj
#prj.save_object("Byz","Byz_data")

frb=prj.to_frb((4, "AU"), [10000,10000])
#plt.savefig("frb.png")
