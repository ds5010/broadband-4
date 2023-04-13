import folium
import pandas as pd
import numpy as np
import geopandas as gpd
import shapely
import matplotlib.pyplot as plt
import matplotlib as mpl
from shapely.geometry import Polygon, LineString, Point


def read_census(file):
    df = pd.read_csv(file, sep=';', dtype={'FULLCODE':str, 'STATE':str, 'COUNTY':str})
    df = df.rename(columns={'FULLCODE':'block_fips'})
    #assert df.shape == shape
    return df

def merge_dataframes(d1, d2, onname, howname):
    d1 = d1.merge(d2, on=onname, how=howname)
    return d1


def plot_block():
    state_speeds = gpd.read_file("data/speeds.json")
    cousub  = read_census("data/DC20BLK_CS2301945810_BLK2MS.txt")

    cousub_speeds = merge_dataframes(state_speeds, cousub, 'block_fips', 'right')
    print(end='\n')
    print(f"The average speed in Millinocket is {cousub_speeds['max_speed'].mean()}")

    #plot
    fig, ax = plt.subplots()
    cousub_speeds.plot(ax=ax, color='lightgray')
    cousub_speeds.plot(ax=ax, column='max_speed', legend=True)
    plt.title('Millinocket Max Advertised Broadband Speed (Mb/s)')
    plt.savefig("img/Millinocket_speeds.png")

if __name__ == "__main__":
    plot_block()
