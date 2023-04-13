import folium
import pandas as pd
import numpy as np
import geopandas as gpd
import shapely
import matplotlib.pyplot as plt
import matplotlib as mpl
from shapely.geometry import Polygon, LineString, Point


def plot_state():
	'''plots state broadband speeds by census block'''

	state_speeds = gpd.read_file('data/speeds.json')

	#plot speeds
	fig, ax = plt.subplots(figsize=(7,8))
	state_speeds.plot(ax=ax, column='max_speed', legend=True, vmax=2000)
	plt.title('Maine Max Advertised Broadband Speeds (Mb/s)')

	plt.savefig('img/Maine_speeds.png')

if __name__ == '__main__':
    plot_state()