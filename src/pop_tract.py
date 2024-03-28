import geopandas as gpd
import pandas as pd
import matplotlib as mpl

# Read Digital-Equity data, one sheet, and filter everything but Maine
filename = "data/county_tract_total_covered_populations.xlsx"
df = pd.read_excel(filename, sheet_name="tract_total_covered_populations")
df = df[(df.geo_id >= 23000000000) & (df.geo_id < 24000000000)]

# Convert FIPS from integer to string so we can merge with the geo-dataframe
df["GEOID"] = df.geo_id.apply(lambda x: str(x))

# Read shapefile
filename = "data/tl_2019_23_tract.zip"
gdf = gpd.read_file(filename)

# Merge geography and dataframe
gdf = gdf.merge(df, on="GEOID")

gdf = gdf[gdf.ALAND != 0]
gdf.tract_tot_pop = gdf.tract_tot_pop.apply(lambda x: None if x == "(X)" else x)

# plot with a continuous colormap
gdf.plot(column='tract_tot_pop', legend=True, vmax=1200, cmap=mpl.cm.inferno);

# Compute population density (people/sq mile) -- recall ALAND is in km
gdf['pop_density'] = gdf.tract_tot_pop / gdf.ALAND * 2589988

# Plot with the colormap that we used before
import numpy as np

# Set up colormap
bounds = np.array([0, 10, 25, 50, 100, 250, 500, 1000, 2500])
norm = mpl.colors.BoundaryNorm(boundaries=bounds, ncolors=256)
cmap = mpl.cm.RdYlGn_r

# Plot
lighter = mpl.colors.ListedColormap(cmap(np.linspace(0.125, 0.875, 256)))
ax = gdf.plot(column='pop_density', cmap=lighter, norm=norm, legend=True)
gdf.boundary.plot(ax=ax, linewidth=0.3, edgecolor='#333')
ax.set_title('Population/mile$^2$ for census tracts');

gdf.to_file("data/pop_tract.json", driver="GeoJSON")

mpl.pyplot.show()


