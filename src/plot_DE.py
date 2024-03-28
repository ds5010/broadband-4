# Necessary imports
import pandas as pd
import geopandas as gpd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as colors

# Set up both DataFrames, convert to strings for merging, merge to create new DataFrame
geo_data = gpd.read_file("data/census_geography_2019.geojson")
de_data = pd.read_csv('data/maine_tract_DE_2019.csv')
geo_data['GEOID'] = geo_data['GEOID'].astype(str)
de_data['GEOID'] = de_data['GEOID'].astype(str)
combined_data = geo_data.merge(de_data, on='GEOID')

# Create population density column
combined_data['tract_tot_pop'] = pd.to_numeric(combined_data['tract_tot_pop'], errors='coerce') # Cleaning data for calculation
combined_data['tract_tot_pop'].fillna(0) # Cleaning data for calculation
combined_data['density'] = combined_data['tract_tot_pop'] / combined_data['ALAND'] * 2589988.11

# Plotting combined data (Lots of credit given to https://github.com/ds5010/spring-2024/blob/main/07-Geo.md)
bounds = np.array([0, 10, 25, 50, 100, 250, 500, 1000, 2500, 5000])
norm = colors.BoundaryNorm(boundaries=bounds, ncolors=256)
cmap = mpl.cm.RdYlGn_r
lighter = colors.ListedColormap(cmap(np.linspace(0.125, 0.875, 256)))
ax = combined_data.plot(column='density', cmap=lighter, norm=norm, legend=True, figsize=(8,8))
combined_data.boundary.plot(ax=ax, linewidth=0.3, edgecolor='#333')
ax.set_title('Population/mile$^2$ for county subdivisions', fontsize=14)
ax.set_xlabel('Longitude', fontsize=12)
ax.set_ylabel('Latitude', fontsize=12)
plt.show()