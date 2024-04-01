import pandas as pd

def get_maine_tract():
    excel = 'https://www2.census.gov/programs-surveys/demo/datasets/community-resilience/county_tract_total_covered_populations.xlsx'
    
    # Specify the sheet_name to grab the right info
    tract_df = pd.read_excel(excel, sheet_name='tract_total_covered_populations')
    tract_df.rename(columns={'geo_id': 'GEOID'}, inplace=True)  # Rename 'geo_id' to 'GEOID' for merging
    maine_tract_info = tract_df[tract_df['GEOID'].astype(str).str[:2] == '23']
    return maine_tract_info

def save_csv(info, filename):
    info.to_csv(filename, index=False)

def main():
    # Get the Maine DE Info Based On Tract
    save_csv(get_maine_tract(), 'data/maine_tract_DE_2019.csv')
if __name__ == "__main__":
    main()
