import geopandas as gpd
import pandas as pd
import json

def create_county_popup_json(filename='../docs/counties_popup.json'):
    info_data = pd.read_excel("../data/county_tract_total_covered_populations.xlsx", sheet_name='county_total_covered_population')
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

        dict[geoid] = {
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

def create_county_json(filename='../docs/counties.json'):
    geo_data = gpd.read_file("../data/tl_2019_us_county.zip")
    geo_data = geo_data[geo_data['STATEFP'] == '23']  # Filter only Maine counties
    geo_data['GEOID'] = geo_data['GEOID'].astype(str)

    with open('../docs/counties_popup.json') as f:
        popup_data = json.load(f)

    popup_df = pd.DataFrame.from_dict(popup_data, orient='index')
    popup_df.index.name = 'GEOID'
    popup_df = popup_df.reset_index()

    combined_data = geo_data.merge(popup_df, on='GEOID')

    combined_data.to_file(filename, driver='GeoJSON')
    print(f"County data saved to {filename}")

def main():
    create_county_popup_json()
    create_county_json()

if __name__ == "__main__":
    main()