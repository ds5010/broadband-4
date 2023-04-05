import pandas as pd
import numpy as np
import geopandas as gpd


print(end='\n')
print("Reading the previously created broadband speeds file")
df = pd.read_csv("data/speeds.csv", dtype={"block_fips":str})

def merge_dataframes(df1, df2, onname, howname):
    df1 = df1.merge(df2, on=onname, how=howname)
    return df1

print(end='\n')
print("Reading the census block file")
print("This may take some time")
filename = "data/tl_2022_23_tabblock20.zip"

stateblock = (filename)

maine_block = gpd.read_file(stateblock, dtype={"GEOID20":str})
maine_block = maine_block[maine_block['ALAND20'] > 0]
maine_block = maine_block.rename(columns={'GEOID20':'block_fips'})

print(end='\n')
print("Merging the two dataframes together")
maine_block = merge_dataframes(maine_block, df, 'block_fips', 'left')

print(end='\n')
print("Writing the merged data to a JSON file")
print("This will take some time")
maine_block.to_file("data/speeds.json", driver="GeoJSON") 
print(end='\n')
print("Complete!")