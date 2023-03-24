import pandas as pd

base = "data/"
filenames = ["bdc_23_Cable_fixed_broadband_063022.zip",
             "bdc_23_Copper_fixed_broadband_063022.zip",
             "bdc_23_Fiber-to-the-Premises_fixed_broadband_063022.zip"]


def read_fcc(filename):
    """
    Read the 'bdc_23_....zip' files in data
    and calculate max download speed

    Params:
    filename - name of file without the path
    """
    df = pd.read_csv(base + filename, compression='zip', dtype={"block_fips":str})
    return df.groupby("block_fips")["max_advertised_download_speed"].max()


block_speeds = {filename.split("_")[2]: read_fcc(filename) 
                for i, filename in enumerate(filenames)}

df = pd.DataFrame(block_speeds)
df["max_speed"] = df.max(axis=1)

df.to_csv(r"data/speeds.csv", sep=',', header=True)