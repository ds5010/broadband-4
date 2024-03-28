# Necessary imports
import geopandas as gpd
import os

# Shapefile for 2019 Maine Census Tract
def get_shapefile(filename='census_geography_2019.geojson', directory='data'):
    '''get_shapefile() grabs the 2019 maine census tract shapefile and saves it as a geoJSON file.
    Parameters: None
    Returns: None, but shapefile is saved as a geoJSON in the data directory.
    '''
    url = 'https://www2.census.gov/geo/tiger/TIGER2019/TRACT/tl_2019_23_tract.zip'
    gdf = gpd.read_file(url)

    # Save as a GeoJSON file
    filepath = os.path.join(directory, filename)
    gdf.to_file(filepath, driver='GeoJSON')
    print(f"GeoJSON file saved as {filepath}")


def main():
    get_shapefile()
if __name__ == "__main__":
    main()