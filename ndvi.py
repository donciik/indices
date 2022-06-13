import numpy as np
import pandas as pd
import geopandas as gpd

import rasterio
import fiona
import shapely
import matplotlib
import rtree
import pyproj


def f_ndvi(in_red, in_nir):
	b4 = rasterio.open(in_red)
	b8 = rasterio.open(in_nir)

	b4_data = b4.read(1).astype('float64')
	b8_data = b8.read(1).astype('float64')
	ndvi = np.where((b8_data + b4_data) == 0, 0, (b8_data - b4_data)/(b8_data + b4_data))
	ndvi[:5,:5]

	ndvi_data = rasterio.open('ndvi.tif','w', driver = 'Gtiff', width = b8.width, height = b8.height, count = 1, crs= b8.crs, transform = b8.transform, dtype = 'float64')
	ndvi_data.write(ndvi,1)
	ndvi_data.close()
	return ndvi_data

