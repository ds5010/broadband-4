import os
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt


def clean_covered_pop(path):
    """
    Cleans data by removing all non-Maine states, replaces empty values,
    corrects column types, saves as CSV
    :param path:
    """
    df = pd.read_excel(path, sheet_name=1)
    df["geo_id"]=df["geo_id"].astype(str)
    df = df[df["geo_id"].str.startswith('23')]
    df = df.fillna(0)
    df = df.replace("(X)", 0)
    df.to_csv("data/covered_pop_tracts.csv", index=False)


def cleaned_df():
    """
    Reads in csv and converts columns to appropriate types
    :return: cleaned dataframe
    """
    df = pd.read_csv("data/covered_pop_tracts.csv")
    df.astype({col: float for col in df.columns[3:]})
    return df


def main():
    clean_covered_pop("data/county_tract_total_covered_populations.xlsx")


if __name__ == "__main__":
    main()
