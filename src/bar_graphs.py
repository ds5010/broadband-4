import matplotlib.pyplot as plt 
import pandas as pd 

file='data/county_tract_total_covered_populations.xlsx'
def clean_file_county(file):
    '''extracts just the maine data by county'''
    county = pd.read_excel(file)  #read file
    county["geo_id"]=county["geo_id"].astype(str)
    county = county[county["geo_id"].str.startswith('23')]  
    county.to_csv('data/county_dii.csv') #Saves the CSV to use 


def graph_data(data, column_name, title, county_nu=16):   #made so can change the number of counties if we really only want to see the top 5 
   '''Input-Data frame- sorts it to the top percentages
        bar graphs'''
   data = data.sort_values(by=column_name, ascending=False)
   highcounties = data[:county_nu].copy() # Added copy to fix the warning.
   highcounties['geography_name'] = highcounties['geography_name'].str.slice(stop=-14) # Removed the redundant parts in the labels
   counties = range(len(highcounties['geography_name']))  
   plt.figure(figsize=(12, 8)) 
   plt.bar(counties, highcounties[column_name], label=column_name)
   
   #Makes labels for bar graphs (Nice Touch Van!!) 
   for i, value in enumerate(highcounties[column_name]):
       plt.text(i, value, f'{value:.2f}%', ha='center', va='bottom')

   plt.xlabel('Maine County', fontsize=14)
   plt.ylabel('Percentage (Covered Populations)', fontsize=14)
   plt.title(f'Maine Counties Ordered by Percent {title} Population', fontsize=16)
   plt.xticks(counties, highcounties['geography_name'], ha='right', rotation=45)  # ha moves the ticks over! 
   plt.tight_layout()
   plt.savefig(f'img/{column_name}_bar.png') #save it 
   plt.close() 

def main():
    clean_file_county(file)
    data = pd.read_csv("data/county_dii.csv")
    graph_data(data, 'pct_lang_barrier_pop', "Language Barrier")
    graph_data(data, 'pct_minority_pop', "Minority")
    graph_data(data, 'pct_dis_pop', "Disability")
    graph_data(data, "pct_rural_pop", "Rural Living")
    graph_data(data, 'pct_vet_pop', "Veteran")
    graph_data(data, 'pct_incarc_pop', "Incarcerated")
    graph_data(data, 'pct_aging_pop', "Age 60+")
    graph_data(data, 'pct_ipr_pop', "Low Income/Poverty")
    

if __name__=='__main__':
    main()
