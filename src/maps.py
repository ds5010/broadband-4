import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
#import contextily as cx
import seaborn as sns
import rasterio as ro
from pandas.core.arrays.interval import NA

url = "https://www2.census.gov/geo/tiger/TIGER2022/TRACT/tl_2022_23_tract.zip"
gdf = gpd.read_file(url, converters={"GEOID": int})
gdf = gdf[gdf['ALAND'] > 0]
url = "https://www2.census.gov/geo/docs/reference/codes/files/st23_me_cousub.txt"
df = pd.read_csv(url, header=None, converters={"county": str},usecols = [2,3],names=["county","name"])
df = df.drop_duplicates(subset="name")
df.set_index('county', drop=True, inplace=True)
diction=df.to_dict(orient='index')

scores = ['DDI', 'INFA', 'SE']

for score in scores:
    df_data=pd.read_csv('data/'+score+'_tract.csv')
    del df_data[df_data.columns[0]]
    df_data['county']=df_data['TractID'].apply(lambda x:str(x)[2:5]+str(x)[-4:])
    df_data['title']=df_data['county'].apply(lambda x: diction[x[:3]]['name']+" tract:"+x[-4:] if x[:3] in diction else NA)
    df_data['GEOID']=df_data['TractID'].astype('str')
    df_data.drop(columns=['TractID'], inplace=True)
    new_gdf = gdf.merge(df_data[['GEOID',score,'title']],on='GEOID', how='left')
    new_gdf.to_file('data/'+score+'.json', driver="GeoJSON")
    print('saving '+score+' GeoJSON data to data/'+score+'.json')
    new_wm = new_gdf.to_crs(epsg=3857)

    print('Plotting ' +score+ ' scores on map')
    bounds = np.array([0,10,20,30,40,50,60,70,80,90])
    norm = mpl.colors.BoundaryNorm(boundaries=bounds, ncolors=256)
    cmap=mpl.cm.RdYlGn_r
    ax = new_wm.plot(score, legend=True, norm=norm, cmap=cmap)
    new_wm.boundary.plot(ax=ax, linewidth=0.2, edgecolor='#333')
    #cx.add_basemap(ax, source=cx.providers.Stamen.TonerLite)
    plt.gcf().set_size_inches(10,10)
    plt.title(label= score+" scores per census tract")
    plt.savefig('img/'+score+'_tract.png', dpi=300)
    plt.show()
    print(end='\n')
    print("Plot saved to img/"+score+"_tract.png \n")
    print("Complete!")
    plt.close()


'''
df_data=pd.read_csv('data/DDI_tract.csv')
del df_data[df_data.columns[0]]
df_data['county']=df_data['TractID'].apply(lambda x:str(x)[2:5]+str(x)[-4:])
df_data['title']=df_data['county'].apply(lambda x: diction[x[:3]]['name']+" tract:"+x[-4:] if x[:3] in diction else NA)
df_data['GEOID']=df_data['TractID'].astype('str')
df_data.drop(columns=['TractID'], inplace=True)
new_gdf = gdf.merge(df_data[['GEOID','DDI_avg','title']],on='GEOID', how='left')
new_gdf.to_file("data/DDI.json", driver="GeoJSON") 
DDI_wm = new_gdf.to_crs(epsg=3857)

print("Plotting DDI scores on map")
bounds = np.array([0,10,20,30,40,50,60,70,80,90])
norm = mpl.colors.BoundaryNorm(boundaries=bounds, ncolors=256)
cmap=mpl.cm.RdYlGn_r
ax = DDI_wm.plot("DDI_avg", legend=True, norm=norm, cmap=cmap)
DDI_wm.boundary.plot(ax=ax, linewidth=0.2, edgecolor='#333')
#cx.add_basemap(ax, source=cx.providers.Stamen.TonerLite)
plt.gcf().set_size_inches(10,10)
plt.title(label="DDI scores per census tract")
plt.savefig("img/DDI_tract.png", dpi=300)
plt.show()
print(end='\n')
print("Plot saved to img/DDI_tract.png \n")
print("Complete!")
plt.close()

df_data=pd.read_csv('data/INFA_tract.csv')
del df_data[df_data.columns[0]]
df_data['county']=df_data['TractID'].apply(lambda x:str(x)[2:5]+str(x)[-4:])
df_data['title']=df_data['county'].apply(lambda x: diction[x[:3]]['name']+" tract:"+x[-4:] if x[:3] in diction else NA)
df_data['GEOID']=df_data['TractID'].astype('str')
df_data.drop(columns=['TractID'], inplace=True)
new_gdf2 = gdf.merge(df_data[['GEOID','INFA','title']],on='GEOID', how='left')
new_gdf2.to_file("data/INFA.json", driver="GeoJSON") 
INFA_wm = new_gdf2.to_crs(epsg=3857)

print("Plotting INFA scores on map")
bounds = np.array([0,10,20,30,40,50,60,70,80,90])
norm = mpl.colors.BoundaryNorm(boundaries=bounds, ncolors=256)
cmap=mpl.cm.RdYlGn_r
ax = INFA_wm.plot("INFA", legend=True, norm=norm, cmap=cmap)
INFA_wm.boundary.plot(ax=ax, linewidth=0.2, edgecolor='#333')
#cx.add_basemap(ax, source=cx.providers.Stamen.TonerLite)
plt.gcf().set_size_inches(10,10)
plt.title(label="INFA scores per census tract")
plt.savefig("img/INFA_tract.png", dpi=300)
plt.show()
print(end='\n')
print("Plot saved to img/INFA_tract.png \n")
print("Complete!")
plt.close()

df_data=pd.read_csv('data/SE_tract.csv')
del df_data[df_data.columns[0]]
df_data['county']=df_data['TractID'].apply(lambda x:str(x)[2:5]+str(x)[-4:])
df_data['title']=df_data['county'].apply(lambda x: diction[x[:3]]['name']+" tract:"+x[-4:] if x[:3] in diction else NA)
df_data['GEOID']=df_data['TractID'].astype('str')
df_data.drop(columns=['TractID'], inplace=True)
new_gdf3 = gdf.merge(df_data[['GEOID','SE','title']],on='GEOID', how='left')
new_gdf3.to_file("data/SE.json", driver="GeoJSON") 
SE_wm = new_gdf3.to_crs(epsg=3857)

print("Plotting SE scores on map")
bounds = np.array([0,10,20,30,40,50,60,70,80,90])
norm = mpl.colors.BoundaryNorm(boundaries=bounds, ncolors=256)
cmap=mpl.cm.RdYlGn_r
ax = SE_wm.plot("SE", legend=True, norm=norm, cmap=cmap)
SE_wm.boundary.plot(ax=ax, linewidth=0.2, edgecolor='#333')
#cx.add_basemap(ax, source=cx.providers.Stamen.TonerLite)
plt.gcf().set_size_inches(10,10)
plt.title(label="SE scores per census tract")
plt.savefig("img/SE_tract.png", dpi=300)
plt.show()
print(end='\n')
print("Plot saved to img/SE_tract.png \n")
print("Complete!")
plt.close()
'''