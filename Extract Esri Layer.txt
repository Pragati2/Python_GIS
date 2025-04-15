Dataframe Extract - GIS Pipeline Layer 

from arcgis.features import FeatureLayer, GeoAccessor
# Establish a connection to your GIS.
from arcgis.gis import GIS

gis = GIS('\*gisportal link*\')

FL = FeatureLayer('https://gisporta')
#esri_p = GeoAccessor.from_layer(FL)‍‍‍

esri_layer = pd.DataFrame.spatial.from_layer(FL)

