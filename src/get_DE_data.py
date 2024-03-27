import pandas as pd

def get_maine_tract():
    tract_df = pd.read_csv('data/tract_total_covered_populations.csv')
    maine_tract_info = tract_df[tract_df['geo_id'].astype(str).str[:2] == '23']
    return maine_tract_info

def get_maine_county():
    county_df = pd.read_csv('data/county_tract_total_covered_population.csv')
    maine_county_info = county_df[county_df['geo_id'].astype(str).str[:2] == '23']
    return maine_county_info

def save_csv(info, filename):
    info.to_csv(filename, index=False)

def main():
    # Get the Maine DE Info Based On Tract
    save_csv(get_maine_tract(), 'data/maine_tract_DE_2019.csv')

    # Get the Maine County Info Based on County
    save_csv(get_maine_county(), 'data/maine_county_DE_2019.csv')

if __name__ == "__main__":
    main()
