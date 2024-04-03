# Necessary Imports
import pandas as pd
import geopandas as gpd
import json

def save_geojson(data, filename):
    data.to_file(filename, driver='GeoJSON')
    print(f"Data saved to {filename}")


def save_dictionary():
    excel = 'https://www2.census.gov/programs-surveys/demo/datasets/community-resilience/county_tract_total_covered_populations.xlsx'
    dictionary_df = pd.read_excel(excel, sheet_name='Tract File Layout', skiprows=4)
    
    dict = {}
    for blah, row in dictionary_df.iterrows():
        name = row['Variable Name']
        dict[name] = {
            "Column": row['Column'],
            "Description": row['Description'],
            "Source(s)": row['Source(s)']
        }
        
    # Save as json file
    with open('docs/dictionary.json', 'w') as file:
        json.dump(dict, file, indent=4)


def main():
    # Set up both DataFrames, convert to strings for merging, merge to create new DataFrame
    geo_data = gpd.read_file("data/census_geography_2019.geojson")
    geo_data = geo_data[geo_data.ALAND != 0] # removes water in maps
    de_data = pd.read_csv('data/maine_tract_DE_2019.csv')
    geo_data['GEOID'] = geo_data['GEOID'].astype(str)
    de_data['GEOID'] = de_data['GEOID'].astype(str)
    combined_data = geo_data.merge(de_data, on='GEOID')
    # Save the data.json file
    save_geojson(combined_data, 'docs/data.json')

    # Save the dictionary.json file
    save_dictionary()

if __name__ == "__main__":
    main()