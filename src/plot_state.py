import folium
import pandas as pd
import numpy as np
import geopandas as gpd
import shapely
import matplotlib.pyplot as plt
import matplotlib as mpl
from shapely.geometry import Polygon, LineString, Point

json_path = "data/speeds.json"
img_path = "img/Maine_speeds.png"

print(end='\n')
print("Reading JSON file with speed info")
print("This can take up to 40 seconds")
state_speeds = gpd.read_file(json_path)

#Creates the plot of broadband speeds.  This is placed over a plot of the state in light gray as some areas may have
#no available broadband.
print(end='\n')
print("Creating plot of the maximum broadband speeds available throughout the state")
print("This can take up to 15 seconds")
fig, ax = plt.subplots(figsize=(7,8))
state_speeds.plot(ax=ax, color='lightgray')
state_speeds.plot(ax=ax, column='max_speed', legend=True, vmax=2000);
plt.savefig(img_path)
print(end='\n')
print("Plot saved to "+img_path)
print("Complete!")
