# Imports
import matplotlib.pyplot as plt 
import pandas as pd 

file='data/county_tract_total_covered_populations.xlsx'
def clean_file_county(file):
    '''extracts just the maine data by county'''
    county = pd.read_excel(file)  #read file
    county["geo_id"]=county["geo_id"].astype(str)
    county = county[county["geo_id"].str.startswith('23')]  
    county.to_csv('data/county_dii.csv') #Saves the CSV to use 


def graph_data(data, column_name, title, county_nu=16):  # Defaults to plotting the top 16 counties
    '''Input-Data frame- sorts it to the top percentages and bar graphs them'''
    data = data.sort_values(by=column_name, ascending=False)
    highcounties = data[:county_nu].copy()  # Get data for the top 16 counties
    highcounties['geography_name'] = highcounties['geography_name'].str.slice(stop=-14)  # Cleaning names

    plt.figure(figsize=(12, 8))
    for blah in range(len(highcounties)): # Iterating over all 16 counties
        if blah < 5:  # Only top 5 are for the legend
            plt.bar(blah, highcounties.iloc[blah][column_name], label=highcounties.iloc[blah]['geography_name'], color='tab:blue')
        else:
            plt.bar(blah, highcounties.iloc[blah][column_name], color='tab:blue')

    # Adding percentages over bars
    for i, value in enumerate(highcounties[column_name]):
        plt.text(i, value, f'{value:.2f}%', ha='center', va='bottom')

    plt.xlabel('Maine County', fontsize=14)
    plt.ylabel('Percentage (Covered Populations)', fontsize=14)
    plt.title(f'Maine Counties Ordered by Percent {title} Population', fontsize=16)
    plt.xticks(range(county_nu), highcounties['geography_name'], rotation=45, ha='right')
    plt.legend(title="Top 5 Counties")  # Legend will now show only for the top 5 counties
    plt.tight_layout()
    plt.savefig(f'figs/bargraphs/{column_name}_bar.png')
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
