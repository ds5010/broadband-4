# Imports
import geopandas as gpd
import pandas as pd
import json
import numpy as np

def json_info_tract(filename='docs/tract_information.json'):
    '''
    this function reads the tract data from the excel file and saves it as a json file called 'tract_information.json'
    :param filename: tract_information.json
    :return: None
    '''
    sheet_name = 'tract_total_covered_populations'
    info_data = pd.read_excel("data/county_tract_total_covered_populations.xlsx", sheet_name=sheet_name)
    info_data = info_data[info_data['geo_id'].astype(str).str[:2] == '23']  # Extracting only Maine data
    info_data['geo_id'] = info_data['geo_id'].astype(str)
    print("Saving tract data to: " + filename)
    dict = {}
    for info, row in info_data.iterrows():
        geoid = row['geo_id']
        tract_name = row['geography_name']
        total_pop = row['tract_tot_pop']
        pct_near_poverty = row['pct_ipr_pop']
        pct_over_60 = row['pct_aging_pop']
        pct_veterans = row['pct_vet_pop']
        pct_disabled = row['pct_dis_pop']
        pct_language_barrier = row['pct_lang_barrier_pop']
        pct_minorities = row['pct_minority_pop']
        pct_rural_pop = row['pct_rural_pop']
        pct_no_bb_or_computer_pop = row['pct_no_bb_or_computer_pop']
        pct_tot_cov_pop = row['pct_tot_cov_pop']

        dict[geoid] = {
            "Name": tract_name,
            "Total Population": total_pop,
            "Percent Near Poverty": pct_near_poverty,
            "Percent Population over 60": pct_over_60,
            "Percent Veterans": pct_veterans,
            "Percent with a Disability": pct_disabled,
            "Percent Language Barrier": pct_language_barrier,
            "Percent Minorities": pct_minorities,
            "Percent Rural Population": pct_rural_pop,
            "Percent No Device or Broadband": pct_no_bb_or_computer_pop,
            "pct_no_bb_or_computer_pop_popup": f"<b>No Computer or Broadband: {pct_no_bb_or_computer_pop}%</b><div><b>{tract_name}</b></div><div>Total Population: {total_pop}</div><div>Percent Near Poverty: {pct_near_poverty}</div><div>Percent Population over 60: {pct_over_60}</div><div>Percent Veterans: {pct_veterans}%</div><div>Percent with a Disability: {pct_disabled}</div><div>Percent Language Barrier: {pct_language_barrier}</div><div>Percent Minorities: {pct_minorities}</div><div>Percent Rural Population: {pct_rural_pop}</div><div>Percent No Device or Broadband: {pct_no_bb_or_computer_pop}</div>",
            "pct_tot_cov_pop_popup": f"<b>Covered Population: {pct_tot_cov_pop}%</b><div><b>{tract_name}</b></div><div>Total Population: {total_pop}</div><div>Percent Near Poverty: {pct_near_poverty}</div><div>Percent Population over 60: {pct_over_60}</div><div>Percent Veterans: {pct_veterans}%</div><div>Percent with a Disability: {pct_disabled}</div><div>Percent Language Barrier: {pct_language_barrier}</div><div>Percent Minorities: {pct_minorities}</div><div>Percent Rural Population: {pct_rural_pop}</div><div>Percent No Device or Broadband: {pct_no_bb_or_computer_pop}</div>"
        }
    
    try:
        with open(filename, 'w') as file:
            json.dump(dict, file, indent=4)
        print('Tract data saved at: ' + filename)
    except Exception as e:
        print('An error occurred while saving the tract data:', str(e))

def create_json(filename='docs/tracts.json'):
    '''
    this function creates a geojson file with the tract data and
    saves calling it 'tracts.json' while merging the tract data with the popup data
    :param filename: tracts.json
    :return: None
    '''
    # Create tract information JSON
    json_info_tract()
    
    # Create dataframes
    geo_data = gpd.read_file("data/tl_2019_23_tract.zip").query('ALAND > 0') # Removes water from maps
    de_data = pd.read_excel("data/county_tract_total_covered_populations.xlsx", sheet_name='tract_total_covered_populations')

    # Clean and merge
    de_data = de_data[de_data['geo_id'].astype(str).str[:2] == '23'] # Extracting only maine data
    de_data['geo_id'] = de_data['geo_id'].astype(str)
    combined_data = geo_data.merge(de_data, left_on='GEOID', right_on='geo_id')
    combined_data['geo_id'] = combined_data['geo_id'].astype(int)

    # Calculate population density
    combined_data['pop_density'] = combined_data['tract_tot_pop'].astype(np.float64) / combined_data['ALAND'] * 2589988
    #Adds HTML String
    combined_data['pct_no_bb_or_computer_pop_popup'] = '<b>No Computer or Broadband: ' + combined_data['pct_no_bb_or_computer_pop'].astype(str) + '%</b><div><b>' + combined_data['geography_name'] + '</b></div><div>Total Population: ' + combined_data['tract_tot_pop'].astype(str) + '</div><div>Percent Near Poverty: ' + combined_data['pct_ipr_pop'].astype(str) + '</div><div>Percent Population over 60: ' + combined_data['pct_aging_pop'].astype(str) + '</div><div>Percent Veterans: ' + combined_data['pct_vet_pop'].astype(str) + '%</div><div>Percent with a Disability: ' + combined_data['pct_dis_pop'].astype(str) + '</div><div>Percent Language Barrier: ' + combined_data['pct_lang_barrier_pop'].astype(str) + '</div><div>Percent Minorities: ' + combined_data['pct_minority_pop'].astype(str) + '</div><div>Percent Rural Population: ' + combined_data['pct_rural_pop'].astype(str) + '</div><div>Percent No Device or Broadband: ' + combined_data['pct_no_bb_or_computer_pop'].astype(str) + '</div>'
    combined_data['pct_tot_cov_pop_popup'] = '<b>Covered Population: ' + combined_data['pct_tot_cov_pop'].astype(str) + '%</b><div><b>' + combined_data['geography_name'] + '</b></div><div>Total Population: ' + combined_data['tract_tot_pop'].astype(str) + '</div><div>Percent Near Poverty: ' + combined_data['pct_ipr_pop'].astype(str) + '</div><div>Percent Population over 60: ' + combined_data['pct_aging_pop'].astype(str) + '</div><div>Percent Veterans: ' + combined_data['pct_vet_pop'].astype(str) + '%</div><div>Percent with a Disability: ' + combined_data['pct_dis_pop'].astype(str) + '</div><div>Percent Language Barrier: ' + combined_data['pct_lang_barrier_pop'].astype(str) + '</div><div>Percent Minorities: ' + combined_data['pct_minority_pop'].astype(str) + '</div><div>Percent Rural Population: ' + combined_data['pct_rural_pop'].astype(str) + '</div><div>Percent No Device or Broadband: ' + combined_data['pct_no_bb_or_computer_pop'].astype(str) + '</div>'

    # Download as geojson in docs directory
    combined_data.to_file(filename, driver='GeoJSON')
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    create_json()