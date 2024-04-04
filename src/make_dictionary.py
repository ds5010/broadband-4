# Necessary Imports
import pandas as pd
import json


def save_dictionary():
    excel = 'https://www2.census.gov/programs-surveys/demo/datasets/community-resilience/county_tract_total_covered_populations.xlsx'
    dictionary_df = pd.read_excel(excel, sheet_name='Tract File Layout', skiprows=4)
    
    dict = {}
    for blah, row in dictionary_df.iterrows():
        name = row['Variable Name']
        dict[name] = {
            "Column": row['Column'],
            "Description": row['Description'],
            "Source(s)": row['Source(s)']
        }
        
    # Save as json file
    with open('docs/dictionary.json', 'w') as file:
        json.dump(dict, file, indent=4)


save_dictionary()