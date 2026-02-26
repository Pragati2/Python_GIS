import xml.etree.ElementTree as ET
import fiona
import pandas as pd
import geopandas as gpd
import requests

def extract_z_geometry(kml_file):
    tree = ET.parse(kml_file)
    root = tree.getroot()
    namespace = {'kml': 'http://www.opengis.net/kml/2.2'}

    coordinates = []
    for placemark in root.findall('.//kml:Placemark', namespace):
        for coord in placemark.findall('.//kml:coordinates', namespace):
            coords_text = coord.text.strip()
            for line in coords_text.split():
                lon, lat, alt = map(float, line.split(','))
                coordinates.append({'Longitude': lon, 'Latitude': lat, 'Altitude': alt})

    return pd.DataFrame(coordinates)
