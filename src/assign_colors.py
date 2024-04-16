import pandas as pd
import geopandas as gpd
import json


def assign_chunks(data_path):

    # Reads in the data and converts to a gdf
    column_df = gpd.read_file(data_path)

    # Skips first columns
    all_chunks = [None, None, None]

    # Iterates through needed columns
    for column in column_df.columns[15:-1]:

        # Max value for the column
        max_value = pd.to_numeric(column_df[column]).max()

        # Chunks/buckets
        chunk = max_value / 5

        # Starts at 0
        chunk_list = [0]

        # Creates remaining chunks
        for i in range(5):
            chunk_list.append(int((i + 1) * chunk))

        # Adds chunks to the chunk list
        all_chunks.append(chunk_list)

    # Returns chunks/buckets for all columns
    return all_chunks


def main():

    chunk_list = assign_chunks("docs/data.json")
    dictionary_df = pd.read_json("docs/dictionary.json").transpose()
    dictionary_df["chunks"] = chunk_list
    dictionary_df["colors"] = 48 * [["#ffffcc", "#c7e9b4", "#7fcdbb",
                                     "#41b6c4", "#2c7fb8", "#253494"]]

    # Maintains original format
    dictionary = dictionary_df.transpose().to_dict()

    with open('../docs/dictionary_with_colors.json', 'w') as file:
        json.dump(dictionary, file, indent=4)


if __name__ == "__main__":
    main()
