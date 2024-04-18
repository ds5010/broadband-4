# Necessary Imports
import geopandas as gpd
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import assign_colors

# List of lists of plot column names, titles and fig filenames, 2 pairs of column name / title and one filename.
plot_list = [
    ["tot_cov_pop", "Total Covered Populations in Tract", "pct_tot_cov_pop", "Percent Covered Populations in Tract", "covered_population"],
    ["ipr_pop", "Total Near Poverty Population", "pct_ipr_pop", "Percent Near Poverty Population Covered", "near_poverty"],
    ["aging_pop", "Tract population age 60 years and older", "pct_aging_pop", "Percent Ages 60+ Populations", "Age 60+"],
    ["incarc_pop", "Tract population incarcerated", "pct_incarc_pop", "Percent Incarcerated Populations", "Incarcerated"],
    ["dis_pop", "Tract population with disability", "pct_dis_pop", "Percent Disability Populations", "Disabled"],
    ["vet_pop", "Tract veteran population", "pct_vet_pop", "Percent Veterans Populations", "Veterans"],
    ["lang_barrier_pop", "Tract population with a language barrier", "pct_lang_barrier_pop", "Percent Language Barrier Populations", "Language Barrier"],
    ["no_bb_or_computer_pop", "Tract household population w/o Broadband or Computers", "pct_no_bb_or_computer_pop", "Percent Population w/o Broadband or Computers", "Lack Broadband or Computers"],
    ["minority_pop", "Tract population of minorities", "pct_minority_pop", "Percent Minority Populations", "Minorities"],
    ["rural_pop", "Tract population living in rural areas", "pct_rural_pop", "Percent Rural Populations", "People in Rural Areas"],
    ["lang_pop", "Tract population ESL 5 years and older", "pct_lang_pop", "Percent ESL 5 years and older", "Non-native English Speakers"]
]

def make_plot(gpd_obj, plot_obj):
    # Plotting combined data 
    
    # Convert the data in the column with these indices to numeric, fill missing values in columns with 0's
    indices_to_convert = [0, 2]
    for index in indices_to_convert:
        gpd_obj[plot_obj[index]] = pd.to_numeric(gpd_obj[plot_obj[index]], errors='coerce')
        gpd_obj[plot_obj[index]] = gpd_obj[plot_obj[index]].fillna(0)  # Data cleaning
    
    color_list = assign_colors.colors[0]

    # Calculate the range for each color
    min_val = gpd_obj[plot_obj[0]].min()
    max_val = gpd_obj[plot_obj[0]].max()
    min_val2 = gpd_obj[plot_obj[2]].min()
    max_val2 = gpd_obj[plot_obj[2]].max()
    interval = (max_val - min_val) / (len(color_list)-1)
    interval2 = (max_val2 - min_val2) / (len(color_list)-1)

    # Define color bins based on the range and color_list
    color_bins_pop = [i * interval for i in range(len(color_list))]
    #color_bins_pop.append(max_val)  # Include the maximum value
    color_bins_pct = [i * interval2 for i in range(len(color_list))]
    #color_bins_pct.append(max_val2)  # Include the maximum value
    
    # Add a negative lower boundary (adjust as needed)
    lower_boundary = -1
    color_bins_pop.insert(0, lower_boundary)
    color_bins_pct.insert(0, lower_boundary)

    # Plotting combined data
    cmap_pop = mpl.colors.ListedColormap(color_list)
    norm_pop = mpl.colors.BoundaryNorm(color_bins_pop, cmap_pop.N)
    cmap_pct = mpl.colors.ListedColormap(color_list)
    norm_pct = mpl.colors.BoundaryNorm(color_bins_pct, cmap_pct.N)
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

    # Left side of fig plot details
    gpd_obj.plot(column=plot_obj[0], cmap=cmap_pop, norm=norm_pop, figsize=(8,8), ax=ax[0])
    gpd_obj.boundary.plot(ax=ax[0], linewidth=0.3, edgecolor='#333')
    ax[0].set_title(plot_obj[1], fontsize=16)
    ax[0].set_xlabel('Longitude', fontsize=12)
    ax[0].set_ylabel('Latitude', fontsize=12)
    
    color_bins_pop_str = [str(round(value)) for value in color_bins_pop]
    color_bins_pop_str[0] = ''
    colorbar = fig.colorbar(ax[0].collections[0], ax=ax[0])  # Assuming a single plot on the axes
    colorbar.ax.set_yticklabels(color_bins_pop_str)  # Example: Set custom tick labels
    
    # Right side of fig plot details
    gpd_obj.plot(column=plot_obj[2], cmap=cmap_pct, norm=norm_pct, figsize=(8,8), ax=ax[1])
    gpd_obj.boundary.plot(ax=ax[1], linewidth=0.3, edgecolor='#333')
    ax[1].set_title(plot_obj[3], fontsize=16)
    ax[1].set_xlabel('Longitude', fontsize=12)
    ax[1].set_ylabel('Latitude', fontsize=12)

    color_bins_pct_str = [str(round(value)) for value in color_bins_pct]
    color_bins_pct_str[0] = ''
    colorbar = fig.colorbar(ax[1].collections[0], ax=ax[1])  # Assuming a single plot on the axes
    colorbar.ax.set_yticklabels(color_bins_pct_str)  # Example: Set custom tick labels
    
    # Formatting
    plt.tight_layout()
        
    # Save and name each figure to the specified file path
    plot_filename = plot_obj[4]
    figs_dir = "figs/tract"
    fig.savefig(f'{figs_dir}/{plot_filename}.png')

# Read geojson file into a geopandas object
gpd_obj = gpd.read_file('docs/tracts.json')

# Iterate through plot lists and call make_plot to create pngs and save each
for plot_obj in plot_list:
    make_plot(gpd_obj, plot_obj)  
  