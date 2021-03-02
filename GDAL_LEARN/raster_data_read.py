from osgeo import gdal, ogr
import pandas as pd
import numpy as np
import os, glob
##
dem_file = 'F:\python_code\gdal_gee\GDAL_LEARN\dem.tif'
ds = gdal.Open(dem_file)
help(ds)

