# Imports
import geopandas as gpd
import pandas as pd

def create_json(filename='docs/counties.json'):
    # Create dataframes
    geo_data = gpd.read_file("https://www2.census.gov/geo/tiger/TIGER2019/COUNTY/tl_2019_us_county.zip")
    de_data = pd.read_excel("data/county_tract_total_covered_populations.xlsx", sheet_name='county_total_covered_population')

    # Clean and merge
    de_data = de_data[de_data['geo_id'].astype(str).str[:2] == '23'] # Extracting only maine data
    de_data['GEOID'] = de_data['geo_id'].astype(str)
    geo_data['GEOID'] = geo_data['GEOID'].str[:5]
    de_data['GEOID'] = de_data['GEOID'].str[:5]
    combined_data = geo_data.merge(de_data, on='GEOID')

    # Download as geojson in docs directory
    combined_data.to_file(filename, driver='GeoJSON')
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    create_json()