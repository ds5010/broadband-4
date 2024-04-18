import pandas as pd
import geopandas as gpd
import json

colors = [["#d73027", "#fc8d59", "#fee090",
           "#e0f3f8", "#91bfdb", "#4575b4"]]


def assign_chunks(data_path, start, end):

    # Reads in the data and converts to a gdf
    column_df = gpd.read_file(data_path)

    # Skips first columns
    all_chunks = [None, None, None]

    # Iterates through needed columns
    for column in column_df.columns[start:end]:

        # Max value for the column
        max_value = pd.to_numeric(column_df[column]).max()

        # Chunks/buckets
        chunk = max_value / 5

        # Starts at 0
        chunk_list = [0]

        # Creates remaining chunks
        for i in range(5):
            if column[0:3] != "pct":
                chunk_list.append(int((i + 1) * chunk))
            else:
                chunk_list.append((i + 1) * chunk)
        # Adds chunks to the chunk list
        chunk_list = [round(item, 2) for item in chunk_list]
        all_chunks.append(chunk_list)



    # Returns chunks/buckets for all columns
    return all_chunks


def main():

    chunk_list = assign_chunks("docs/tracts.json", 15, -4)
    dictionary_df = pd.read_json("docs/dictionary.json").transpose()
    dictionary_df["domain"] = chunk_list
    dictionary_df["range"] = 48 * colors

    # Maintains original format
    dictionary = dictionary_df.transpose().to_dict()

    with open('docs/dictionary_tracts.json', 'w') as file:
        json.dump(dictionary, file, indent=4)

    chunk_list_2 = assign_chunks("docs/counties.json", 20, -4)
    dictionary_df_2 = pd.read_json("docs/dictionary_county.json").transpose()
    dictionary_df_2["domain"] = chunk_list_2
    dictionary_df_2["range"] = 51 * colors

    # Maintains original format
    dictionary_2 = dictionary_df_2.transpose().to_dict()

    with open('docs/dictionary_counties.json', 'w') as file:
        json.dump(dictionary_2, file, indent=4)


if __name__ == "__main__":
    main()
