import geopandas as gpd
import pandas as pd
import json

def json_info_tract(filename='../docs/tract_information.json'):
    '''
    This function reads the tract data from the excel file and saves it as a json file called 'tract_information.json'
    :param filename: the name of the file to save the json data
    :return: None
    '''
    sheet_name = 'tract_total_covered_populations'
    info_data = pd.read_excel("../data/county_tract_total_covered_populations.xlsx", sheet_name=sheet_name)
    info_data = info_data[info_data['geo_id'].astype(str).str[:2] == '23']
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

def create_json(filename='../docs/tracts.json'):
    '''
    this function creates a geojson file with the tract data and saves calling it 'tracts.json'
    :param filename: the name of the file to save the geojson data
    :return: None
    '''
    json_info_tract()

    geo_data = gpd.read_file("../data/tl_2019_23_tract.zip").query('ALAND > 0')
    geo_data['GEOID'] = geo_data['GEOID'].astype(str)

    with open('../docs/tract_information.json') as f:
        tract_info_data = json.load(f)

    tract_info_df = pd.DataFrame.from_dict(tract_info_data, orient='index')
    tract_info_df.index.name = 'GEOID'
    tract_info_df = tract_info_df.reset_index()

    combined_data = geo_data.merge(tract_info_df, on='GEOID')

    combined_data.to_file(filename, driver='GeoJSON')
    print(f"Tract data saved to {filename}")

if __name__ == "__main__":
    create_json()