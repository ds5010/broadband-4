# Necessary imports
import pandas as pd
import geopandas as gpd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as colors


def make_plot(combined_data, column, title):
    # Extra cleaning
    combined_data[column] = pd.to_numeric(combined_data[column], errors='coerce') # Cleaning data for calculation
    combined_data[column].fillna(0) # Cleaning data for calculation

    # Plotting combined data (Lots of credit given to https://github.com/ds5010/spring-2024/blob/main/07-Geo.md)
    cmap = mpl.cm.RdYlGn_r
    lighter = colors.ListedColormap(cmap(np.linspace(0.125, 0.875, 256)))
    ax = combined_data.plot(column=column, cmap=lighter, legend=True, figsize=(8,8))
    combined_data.boundary.plot(ax=ax, linewidth=0.3, edgecolor='#333')
    ax.set_title(title, fontsize=14)
    ax.set_xlabel('Longitude', fontsize=12)
    ax.set_ylabel('Latitude', fontsize=12)
    plt.show()

def main():
    # Set up both DataFrames, convert to strings for merging, merge to create new DataFrame
    geo_data = gpd.read_file("data/census_geography_2019.geojson")
    de_data = pd.read_csv('data/maine_tract_DE_2019.csv')
    geo_data['GEOID'] = geo_data['GEOID'].astype(str)
    de_data['GEOID'] = de_data['GEOID'].astype(str)
    combined_data = geo_data.merge(de_data, on='GEOID')

    # Make the plots
    make_plot(combined_data, "pct_ipr_pop", "Percent Covered Households Populations")
    make_plot(combined_data, "pct_aging_pop", "Percent Ages 60+ Populations")
    make_plot(combined_data, "pct_incarc_pop", "Percent Incarcerated Populations")
    make_plot(combined_data, "pct_dis_pop", "Percent Disability Populations")
    make_plot(combined_data, "pct_vet_pop", "Percent Veterans Populations")
    make_plot(combined_data, "pct_lang_barrier_pop", "Percent Language Barrier Populations")
    make_plot(combined_data, "pct_no_bb_or_computer_pop", "Percent Population w/o Broadband or Computers")
    make_plot(combined_data, "pct_minority_pop", "Percent Minority Populations")
    make_plot(combined_data, "pct_rural_pop", "Percent Rural Populations")
    make_plot(combined_data, "pct_lang_pop", "Percent ESL")
if __name__ == "__main__":
    main()