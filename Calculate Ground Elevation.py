import geopandas as gpd
import requests
import fiona
import pandas as pd

def get_elevation(lat, lon):
    api_url = f"https://api.opentopodata.org/v1/test-dataset?locations={lat},{lon}"
    response = requests.get(api_url)
    if response.status_code == 200:
        elevation = response.json()['results'][0]['elevation']
        return elevation
    else:
        return None
