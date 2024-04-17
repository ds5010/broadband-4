import geopandas as gpd
import pandas as pd
import json

def create_county_popup_json(filename='docs/counties_popup.json'):
    '''
    this function reads the county data from the excel file and saves it as a json file called 'counties_popup.json'
    :param filename: the name of the file to save the json data
    :return: None
    '''
    info_data = pd.read_excel("data/county_tract_total_covered_populations.xlsx", sheet_name='county_total_covered_population') # Read the county data
    info_data = info_data[info_data['geo_id'].astype(str).str[:2] == '23']
    info_data['geo_id'] = info_data['geo_id'].astype(str)
    print("Saving county popup data to: " + filename)
    dict = {}
    for info, row in info_data.iterrows(): 
        geoid = row['geo_id']
        county_name = row['geography_name']
        total_pop = row['county_tot_pop']
        pct_near_poverty = row['pct_ipr_pop']
        pct_over_60 = row['pct_aging_pop']
        pct_veterans = row['pct_vet_pop']
        pct_disabled = row['pct_dis_pop']
        pct_language_barrier = row['pct_lang_barrier_pop']
        pct_minorities = row['pct_minority_pop']
        pct_rural_pop = row['pct_rural_pop']
        pct_no_device_or_broadband = row['pct_no_bb_or_computer_pop']
        pct_no_fixed_bb_pop_fcc = row['pct_no_fixed_bb_pop_fcc']
        pct_no_bb_or_computer_pop = row['pct_no_bb_or_computer_pop']
        pct_tot_cov_pop = row['pct_tot_cov_pop']

        dict[geoid] = { # Create a dictionary with the county data for each county in Maine
            "Name": county_name,
            "Total Population": total_pop,
            "Percent Near Poverty": pct_near_poverty,
            "Percent Population over 60": pct_over_60,
            "Percent Veterans": pct_veterans,
            "Percent with a Disability": pct_disabled,
            "Percent Language Barrier": pct_language_barrier,
            "Percent Minorities": pct_minorities,
            "Percent Rural Population": pct_rural_pop,
            "Percent No Device or Broadband": pct_no_device_or_broadband,
            "pct_no_fixed_bb_pop_fcc_popup": f"<b>No Fixed Broadband: {pct_no_fixed_bb_pop_fcc}%</b><div><b>{county_name}</b></div><div>Total Population: {total_pop}</div><div>Percent Near Poverty: {pct_near_poverty}</div><div>Percent Population over 60: {pct_over_60}</div><div>Percent Veterans: {pct_veterans}%</div><div>Percent with a Disability: {pct_disabled}</div><div>Percent Language Barrier: {pct_language_barrier}</div><div>Percent Minorities: {pct_minorities}</div><div>Percent Rural Population: {pct_rural_pop}</div><div>Percent No Device or Broadband: {pct_no_device_or_broadband}</div>",
            "pct_no_bb_or_computer_pop_popup": f"<b>No Computer or Broadband: {pct_no_bb_or_computer_pop}%</b><div><b>{county_name}</b></div><div>Total Population: {total_pop}</div><div>Percent Near Poverty: {pct_near_poverty}</div><div>Percent Population over 60: {pct_over_60}</div><div>Percent Veterans: {pct_veterans}%</div><div>Percent with a Disability: {pct_disabled}</div><div>Percent Language Barrier: {pct_language_barrier}</div><div>Percent Minorities: {pct_minorities}</div><div>Percent Rural Population: {pct_rural_pop}</div><div>Percent No Device or Broadband: {pct_no_device_or_broadband}</div>",
            "pct_tot_cov_pop_popup": f"<b>Covered Population: {pct_tot_cov_pop}%</b><div><b>{county_name}</b></div><div>Total Population: {total_pop}</div><div>Percent Near Poverty: {pct_near_poverty}</div><div>Percent Population over 60: {pct_over_60}</div><div>Percent Veterans: {pct_veterans}%</div><div>Percent with a Disability: {pct_disabled}</div><div>Percent Language Barrier: {pct_language_barrier}</div><div>Percent Minorities: {pct_minorities}</div><div>Percent Rural Population: {pct_rural_pop}</div><div>Percent No Device or Broadband: {pct_no_device_or_broadband}</div>"
        }

    try:
        with open(filename, 'w') as file:
            json.dump(dict, file, indent=4)
        print('County popup data saved at: ' + filename)
    except Exception as e:
        print('An error occurred while saving the county popup data:', str(e))

def create_county_json(filename='docs/counties.json'):
    '''
    this function creates a geojson file with the county data and 
    saves calling it 'counties.json'
    :param filename: the name of the file to save the geojson data
    :return: None
    '''
    # Create county information JSON
    create_county_popup_json()

    # Create Dataframes
    geo_data = gpd.read_file("data/tl_2019_us_county.zip").query('ALAND > 0')
    de_data = pd.read_excel("data/county_tract_total_covered_populations.xlsx", sheet_name='county_total_covered_population')
    
    # Clean and Merge
    de_data = de_data[de_data['geo_id'].astype(str).str[:2] == '23'] # Extracting only maine data
    de_data['GEOID'] = de_data['geo_id'].astype(str)
    geo_data['GEOID'] = geo_data['GEOID'].str[:5]
    de_data['GEOID'] = de_data['GEOID'].str[:5]
    combined_data = geo_data.merge(de_data, on='GEOID')

    combined_data['pct_no_bb_or_computer_pop_popup'] = '<b>No Computer or Broadband: ' + combined_data['pct_no_bb_or_computer_pop'].astype(str) + '%</b><div><b>' + combined_data['geography_name'] + '</b></div><div>Total Population: ' + combined_data['county_tot_pop'].astype(str) + '</div><div>Percent Near Poverty: ' + combined_data['pct_ipr_pop'].astype(str) + '</div><div>Percent Population over 60: ' + combined_data['pct_aging_pop'].astype(str) + '</div><div>Percent Veterans: ' + combined_data['pct_vet_pop'].astype(str) + '%</div><div>Percent with a Disability: ' + combined_data['pct_dis_pop'].astype(str) + '</div><div>Percent Language Barrier: ' + combined_data['pct_lang_barrier_pop'].astype(str) + '</div><div>Percent Minorities: ' + combined_data['pct_minority_pop'].astype(str) + '</div><div>Percent Rural Population: ' + combined_data['pct_rural_pop'].astype(str) + '</div><div>Percent No Device or Broadband: ' + combined_data['pct_no_bb_or_computer_pop'].astype(str) + '</div>'
    combined_data['pct_tot_cov_pop_popup'] = '<b>Covered Population: ' + combined_data['pct_tot_cov_pop'].astype(str) + '%</b><div><b>' + combined_data['geography_name'] + '</b></div><div>Total Population: ' + combined_data['county_tot_pop'].astype(str) + '</div><div>Percent Near Poverty: ' + combined_data['pct_ipr_pop'].astype(str) + '</div><div>Percent Population over 60: ' + combined_data['pct_aging_pop'].astype(str) + '</div><div>Percent Veterans: ' + combined_data['pct_vet_pop'].astype(str) + '%</div><div>Percent with a Disability: ' + combined_data['pct_dis_pop'].astype(str) + '</div><div>Percent Language Barrier: ' + combined_data['pct_lang_barrier_pop'].astype(str) + '</div><div>Percent Minorities: ' + combined_data['pct_minority_pop'].astype(str) + '</div><div>Percent Rural Population: ' + combined_data['pct_rural_pop'].astype(str) + '</div><div>Percent No Device or Broadband: ' + combined_data['pct_no_bb_or_computer_pop'].astype(str) + '</div>'

    # Download as geojson in docs directory
    combined_data.to_file(filename, driver='GeoJSON')
    print(f"County data saved to {filename}")

def main():
    create_county_json()

if __name__ == "__main__":
    main()