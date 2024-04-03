import geopandas as gpd
import pandas as pd


def create_json():

    #create dataframes from files in the data directory
    gdf = gpd.read_file("data/tl_2019_23_tract.zip")
    df = pd.read_excel("data/county_tract_total_covered_populations.xlsx", sheet_name=1, dtype={'geo_id': object})
    
    # Clean up xlsx file
    # Filter rows where 'geo_id' column begins with Maine's ID of '23'
    df = df[df['geo_id'].astype(str).str.startswith('23')]

    # Specify the column range for numeric conversion (D through AV)
    numeric_columns = df.columns[3:48]  # Columns D through AV (zero-based indexing)

    # Convert specified columns to numeric
    df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')
    
    # merge the dataframes
    merged = pd.merge(left=gdf, right=df, left_on="GEOID", right_on="geo_id", how='left')
    
    # clean up geographies
    merged = merged[merged['ALAND'] > 0] #remove land area = 0
    
    # Save as a GeoJSON file
    merged.to_file("docs/digital-equity.geojson", driver='GeoJSON')
    print(f"\"digital-equity.geojson\" saved as geojson file in the ./docs folder")

if __name__ == "__main__":
    create_json()