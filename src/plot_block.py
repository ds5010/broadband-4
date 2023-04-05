import folium
import pandas as pd
import numpy as np
import geopandas as gpd
import shapely
import matplotlib.pyplot as plt
import matplotlib as mpl
from shapely.geometry import Polygon, LineString, Point


json_path = "data/speeds.json"
#cousubfile = ('https://www2.census.gov/geo/maps/DC2020/DC20BLK/st23_me/cousub/cs2301945810_millinocket/DC20BLK_CS2301945810_BLK2MS.txt')
img_path = "img/Millinocket_speeds.png"

print(end='\n')
print("Reading JSON file with speed information")
print("This can take up to 40 seconds")
state_speeds = gpd.read_file(json_path)

def read_census(file):
    df = pd.read_csv(file, sep=';', dtype={'FULLCODE':str, 'STATE':str, 'COUNTY':str})
    df = df.rename(columns={'FULLCODE':'block_fips'})
    #assert df.shape == shape
    return df

print(end='\n')
print("Fetching subdivision information from data folder")
filename = "data/DC20BLK_CS2301945810_BLK2MS.txt"
cousub  = read_census(filename)

print(end='\n')
print("Merging the two dataframes")   
def merge_dataframes(d1, d2, onname, howname):
    d1 = d1.merge(d2, on=onname, how=howname)
    return d1

cousub_speeds = merge_dataframes(state_speeds, cousub, 'block_fips', 'right')
print(end='\n')
print(f"The average speed in Millinocket is {cousub_speeds['max_speed'].mean()}")

print(end='\n')
print("Creating plot of the maximum broadband speeds available throughout Millinocket")
print("This can take up to 15 seconds")
fig, ax = plt.subplots(figsize=(7,8))
cousub_speeds.plot(ax=ax, color='lightgray')
cousub_speeds.plot(ax=ax, column='max_speed', legend=True);
plt.savefig(img_path)
print(end='\n')
print("Plot saved to "+img_path)
print("Complete!")
