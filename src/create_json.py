import pandas as pd
import geopandas as gpd


def speedGeo():
    ''' Merges block broadband speeds with census geographies and saves to a json file'''

    #speeds data
    speeds = pd.read_csv("data/speeds.csv", dtype={"block_fips":str})

    #census geographies data
    filename = "data/tl_2022_23_tabblock20.zip"
    maine_block = gpd.read_file(filename, dtype={"GEOID20":str})

    #clean up geographies
    maine_block = maine_block[maine_block['ALAND20'] > 0] #remove land area = 0

    #merge data
    maine_block = maine_block.merge(speeds, left_on = 'GEOID20', right_on = 'block_fips')

    #save desired data
    final = maine_block[['block_fips', 'max_speed', 'geometry']]
    final.to_file("data/speeds.json", driver="GeoJSON") 

if __name__ == "__main__":
    speedGeo()