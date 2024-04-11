import pandas as pd 
import json 

def json_info():
    info_data = pd.read_excel("../data/county_tract_total_covered_populations.xlsx")
    info_data = info_data[info_data['geo_id'].astype(str).str[:2] == '23'] # Extracting only maine data
    info_data['geo_id'] = info_data['geo_id'].astype(str)
    
    file_location = '../docs/popup_information.json'
    dict = {}
    for info, row in info_data.iterrows():
        County = row['geography_name'][:-7]
        dict[County] = {
            "County Total Population: ": row['county_tot_pop'],
            "DDI Total Population: ": row['tot_cov_pop'],
            "Percent Near Poverty: ": row['pct_ipr_pop'],
            "Percent Population over 60: ": row['pct_aging_pop'],
            "Percent Veterans: ": row['pct_vet_pop'],
            'Percent Disabled: ': row['pct_dis_pop'],
            'Percent Language Barrier: ' : row['pct_lang_barrier_pop'],
            'Percent Minorities: ' : row['pct_minority_pop'],
            'Percent Rural Population: ' : row['pct_rural_pop'],
            'Percent No Device or Broadband: ' : row ['pct_no_bb_or_computer_pop']
        }
    
    try:
        # Save as json file
        with open(file_location, 'w') as file:
            json.dump(dict, file, indent=4)
        print('Location: ' + file_location)
    except Exception as e:
        print('An error occurred while saving the file:', str(e))

json_info()
