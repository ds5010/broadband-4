import pandas as pd
import requests
import json
from scipy.stats import zscore
import numpy as np

# QUESTION - SHOULD WE REMOVE ANY AND ALL ACTIVE KEYS?
# Setup variables for API request needed for NIA and NCD scores
MY_KEY = '083b3312e02e0ad2dc088fbed3f8c669097c2e45'

url = 'https://api.census.gov/data/2021/acs/acs5'
params = {
    'get': 'B28002_013E,B11016_001E,B28001_002E,B01003_001E', 
    'for': 'tract:*',
    'in' : 'state:23&in=county:*',
    'key': MY_KEY
}
# Make the API request and parse the response
response = requests.get(url, params=params)
data = json.loads(response.text)

dfacs = pd.DataFrame(data[1:], columns = data[0], dtype = str)
dfacs = dfacs.rename(columns = {'B28002_013E' : 'Houses NIA', 'B11016_001E' : 'Total Houses', 'B28001_002E' : 'Houses w/ CD', 'B01003_001E' : 'Total Pop', 'block group' : 'group'})
dfacs['tract group'] = dfacs.state + dfacs.county + dfacs.tract
dfacs['percent NCD'] = 1 - dfacs['Houses w/ CD'].astype(int) / dfacs['Total Houses'].astype(int)
dfacs['percent NIA'] = dfacs['Houses NIA'].astype(int) / dfacs['Total Houses'].astype(int)
dfz = dfacs[['tract group','percent NIA','percent NCD']].copy()
dfz['NIA_z'] = (dfacs['percent NIA'] - dfacs['percent NIA'].mean())/dfacs['percent NIA'].std()
dfz['NCD_z'] = (dfacs['percent NCD'] - dfacs['percent NCD'].mean())/dfacs['percent NCD'].std()

# Retrieve information for and calculate NBBND scores
base = "data/"
filenames = ["bdc_23_Cable_fixed_broadband_063022.zip",
             "bdc_23_Copper_fixed_broadband_063022.zip",
             "bdc_23_Fiber-to-the-Premises_fixed_broadband_063022.zip",
             "bdc_23_Licensed-Fixed-Wireless_fixed_broadband_063022.zip"]

def read_fcc(filename,columnname):
    """
    Read the 'bdc_23_....zip' files in data
    and calculate max download speed
    Params:
    filename - name of file without the path
    """
    df = pd.read_csv(base + filename, dtype={'block_geoid':str})
    df = df.rename(columns={"block_geoid": "block_fips"})
    return df.groupby("block_fips")[columnname].max()

def get_clean_max(df):
  df["max"]=df.max(axis=1)
  df.drop(columns=["Cable","Copper","Fiber-to-the-Premises","Licensed-Fixed-Wireless"],inplace=True)
  return df

def fun(download,upload):
  if (download>=100 and upload>=20):
    return 1
  return 0

block_download_speeds = {filename.split("_")[2]: read_fcc(filename,"max_advertised_download_speed") 
                for i, filename in enumerate(filenames)}
block_upload_speeds = {filename.split("_")[2]: read_fcc(filename,"max_advertised_upload_speed") 
                for i, filename in enumerate(filenames)}
df = pd.DataFrame(block_download_speeds)
df=get_clean_max(df)
df2 = pd.DataFrame(block_upload_speeds)
df2=get_clean_max(df2)
df=df.merge(df2, how='left', on='block_fips')
df['mean_max_advertised_download_speed']=df['max_x']
df['mean_max_advertised_upload_speed']=df['max_y']
df.drop(columns=['max_x','max_y'],inplace=True)
df=df.reset_index()
df['Percent_of_blocks_with_100_20']=df.apply(lambda x:fun(x.mean_max_advertised_download_speed,x.mean_max_advertised_upload_speed),axis=1)
df['block_fips']=df['block_fips'].apply(lambda x: str(x)[:-4])
df=df.groupby('block_fips').mean()
df=df.reset_index()
df['Percent_of_blocks_without_100_20']=1-df.Percent_of_blocks_with_100_20
df['NBBND_z'] = (df['Percent_of_blocks_without_100_20'] - df['Percent_of_blocks_without_100_20'].mean())/df['Percent_of_blocks_without_100_20'].std()
df = df.rename(columns={"block_fips": "tract group"})
dfz = dfz.merge(df, on='tract group')
scores = dfz[['tract group', 'NIA_z', 'NCD_z','NBBND_z']]

# Retrieve information for and calculate scores for DNS and UPS
df = pd.read_csv("data/bdc_23_Cable_fixed_broadband_063022.zip")
df1 = pd.read_csv("data/bdc_23_Copper_fixed_broadband_063022.zip")
df2 = pd.read_csv("data/bdc_23_Fiber-to-the-Premises_fixed_broadband_063022.zip")
df3 = pd.read_csv('data/bdc_23_Licensed-Fixed-Wireless_fixed_broadband_063022.zip')
df4 = pd.concat([df, df1, df2, df3], axis = 0)
print((df4['max_advertised_download_speed'] == 0).sum())
print((df4['max_advertised_upload_speed'] == 0).sum())
df4.drop(df4[df4.max_advertised_download_speed == 0].index, inplace = True)

dfnew = df4[['block_geoid', 'max_advertised_download_speed', 'max_advertised_upload_speed']].copy()
dfnew['block_geoid'] = dfnew['block_geoid'].astype(str)
dfnew['block group'] = dfnew['block_geoid'].str[0:11]
del dfnew['block_geoid']
median_download = dfnew.groupby('block group')[['max_advertised_download_speed']].apply(np.median)
median_upload = dfnew.groupby('block group')[['max_advertised_upload_speed']].apply(np.median)
median_download.name = 'DNS_median'
median_upload.name = 'UPS_median'
max_download = dfnew.groupby('block group')[['max_advertised_download_speed']].max()
max_upload = dfnew.groupby('block group')[['max_advertised_upload_speed']].max()
max_download = max_download.rename(columns={'max_advertised_download_speed': 'DNS_max'})
max_upload = max_upload.rename(columns={'max_advertised_upload_speed': 'UPS_max'})
avg_download = dfnew.groupby('block group')[['max_advertised_download_speed']].mean()
avg_upload = dfnew.groupby('block group')[['max_advertised_upload_speed']].mean()
avg_download = avg_download.rename(columns={'max_advertised_download_speed': 'DNS_avg'})
avg_upload = avg_upload.rename(columns={'max_advertised_upload_speed': 'UPS_avg'})

dfnew = dfnew.groupby('block group').max()
dfnew = dfnew.join(median_download, on=['block group'])
dfnew = dfnew.join(median_upload, on=['block group'])
dfnew = dfnew.join(max_download, on=['block group'])
dfnew = dfnew.join(max_upload, on=['block group'])
dfnew = dfnew.join(avg_download, on=['block group'])
dfnew = dfnew.join(avg_upload, on=['block group'])
dfnew = dfnew.reset_index()

del dfnew['max_advertised_download_speed']
del dfnew['max_advertised_upload_speed']
numeric_cols = list(dfnew.select_dtypes(include=[np.number]).columns)
for cols in numeric_cols:
  col_zscore = cols + '_z'
  dfnew[col_zscore] = zscore(dfnew[cols])
del dfnew['DNS_median']
del dfnew['UPS_median']
del dfnew['DNS_max']
del dfnew['UPS_max']
del dfnew['DNS_avg']
del dfnew['UPS_avg']

dfnew = dfnew.rename(columns={"block group": "tract group"})
scores = scores.merge(dfnew, on='tract group')
scores['INFA_median'] = scores['NBBND_z']*.3 + scores['NIA_z']*.3 + scores['NCD_z']*.3 -scores['DNS_median_z']*.05 - scores['UPS_median_z']*.05
scores['INFA_max'] = scores['NBBND_z']*.3 + scores['NIA_z']*.3 + scores['NCD_z']*.3 -scores['DNS_max_z']*.05 - scores['UPS_max_z']*.05
scores['INFA_avg'] = scores['NBBND_z']*.3 + scores['NIA_z']*.3 + scores['NCD_z']*.3 -scores['DNS_avg_z']*.05 - scores['UPS_avg_z']*.05
scores = scores.rename(columns={"tract group":"TractID"})

# Gather information for and calculate all SE scores
keys = ['B01001_001E','B01001_020E','B01001_021E','B01001_044E','B01001_045E',
    'B01001_022E','B01001_023E','B01001_046E','B01001_047E','B01001_024E','B01001_025E','B01001_048E',
    'B01001_049E','B17001_002E','B16010_002E','C18108_007E','C18108_008E','C18108_011E','C18108_012E',
    'B28006_002E','B28004_025E','B28004_013E','B28004_009E','B28004_005E']

# construct the url
base = "https://api.census.gov/data/2021/acs/acs5?get="
geog = "&for=tract:*&in=state:23&in=county:*"
url = base + ",".join(keys) + geog
df=pd.read_json(url)

def df_index_reset(df):
  # set the columns from the first row
  df.columns = df.iloc[0]
  # drop the first row
  df.drop(index=0, inplace=True)
  # reset the index
  df.reset_index(drop=True, inplace=True)

df_index_reset(df)
# set the table for integer figures while making the location data strings
df.iloc[:, :-3] = df.iloc[:, :-3].astype(int)
df.iloc[:,-3:] = df.iloc[:,-3:].astype(str)

df.rename(columns = {'B01001_001E':'Total Pop'}, inplace = True)
df.rename(columns = {'B17001_002E':'Below Poverty Level'}, inplace = True)
df.rename(columns = {'B16010_002E':'Less than HS Grad'}, inplace = True)
df.rename(columns = {'B28006_002E':'Less than HS Grad or Equiv'}, inplace = True)
df.rename(columns = {'B28004_025E':'>75K without internet'}, inplace = True)

df['Over 65 pop'] = df.iloc[:, 1:12].sum(axis=1).astype(int)
df['Disabled'] = df.iloc[:, 15:19].sum(axis=1).astype(int)
df['<35K without internet'] = df.iloc[:, 21:24].sum(axis=1).astype(int)
df['TractID'] = df['state']+df['county']+df['tract']

# pulling out the essentials
df2 = df[['TractID', 'Total Pop', 'Over 65 pop', 'Below Poverty Level', 'Less than HS Grad', 'Less than HS Grad or Equiv', 'Disabled', '<35K without internet', '>75K without internet']]
df2.iloc[:,:1] = df2.iloc[:,:1].astype(str)
df2.iloc[:,1:] = df2.iloc[:,1:].astype(int)

# fixing divide by zero issues for percentage of pop by changing denominator to 0.01 -- if no pop percentage will still be zero
# df2['Total Pop'] = df2['Total Pop'].replace(0, 0.01)
# removing the seven tracts with zero pop instead - Based on census tract dissolve polygons they don't contain any land 400=400 tracts in each df
df2 = df2[df2['Total Pop'] != 0]
def calc_percent_Z(df, num_col, denom_col, percent_col, Z_col):
  '''
  Parameters -- dataframe, column name for numerator, column name for denominator, column name for perent calc and column name for Z score
  Function -- creates new columns for percentage of column_num/column_den per row and Z score based on row observations
  Returns the data frame with additional data
  '''
  df[percent_col] = df[num_col]/df[denom_col]
  column_mean = df[percent_col].mean()
  column_std = df[percent_col].std()
  df[Z_col] = (df[percent_col]-column_mean)/column_std

calc_percent_Z(df2, 'Over 65 pop', 'Total Pop', '> 65%', '> 65% Z')
calc_percent_Z(df2, 'Below Poverty Level', 'Total Pop', 'Below Poverty Level%', 'Below Poverty Level% Z')
calc_percent_Z(df2, 'Less than HS Grad', 'Total Pop', 'Less than HS Grad%', 'Less than HS Grad% Z')
calc_percent_Z(df2, 'Less than HS Grad or Equiv', 'Total Pop', 'Less than HS Grad or Equiv%', 'Less than HS Grad or Equiv% Z')
calc_percent_Z(df2, 'Disabled', 'Total Pop', 'Disabled%', 'Disabled% Z')
calc_percent_Z(df2, '<35K without internet', 'Total Pop', '<35K without internet%', '<35K without internet% Z')
calc_percent_Z(df2, '>75K without internet', 'Total Pop', '>75K without internet%', '>75K without internet% Z')

df2['SE Z'] = (.25 * df2['> 65% Z']) + (.25 * df2['Below Poverty Level% Z']) + (.25*df2['Less than HS Grad% Z']) + (.25*df2['Disabled% Z'])
df_ZScore = df2[['TractID', 'Total Pop','> 65% Z','Below Poverty Level% Z','Less than HS Grad% Z','Disabled% Z','<35K without internet% Z','>75K without internet% Z','SE Z']]

scores = scores.merge(df_ZScore[['SE Z', 'TractID']], on='TractID')
scores['DDI_median'] = scores['INFA_median'] + scores['SE Z']
scores['DDI_avg'] = scores['INFA_avg'] + scores['SE Z']
scores['DDI_max'] = scores['INFA_max'] + scores['SE Z']

# Calculate DDI scores for all DNS and UPS configurations
DDI = scores[['TractID', 'DDI_median', 'DDI_avg', 'DDI_max']]
DDI['DDI_median'] = 100*(DDI['DDI_median']-DDI['DDI_median'].min())/(DDI['DDI_median'].max()-DDI['DDI_median'].min())
DDI['DDI_avg'] = 100*(DDI['DDI_avg']-DDI['DDI_avg'].min())/(DDI['DDI_avg'].max()-DDI['DDI_avg'].min())
DDI['DDI_max'] = 100*(DDI['DDI_max']-DDI['DDI_max'].min())/(DDI['DDI_max'].max()-DDI['DDI_max'].min())

print(DDI)
print(DDI.describe())

DDI_avg = DDI[['TractID', 'DDI_avg']]
DDI_avg.to_csv('data/DDI_avg_speeds.csv')
DDI_max = DDI[['TractID', 'DDI_max']]
DDI_max.to_csv('data/DDI_max_speeds.csv')
DDI_median = DDI[['TractID', 'DDI_median']]
DDI_median.to_csv('data/DDI_median_speeds.csv')