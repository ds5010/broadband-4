import pandas as pd
import matplotlib as plt

millinocket = "data/DC20BLK_CS2301945810_BLK2MS.txt"

def compute_bb():
    
    place = pd.read_csv(millinocket, sep=";")
    speed = pd.read_csv("data/speeds.csv")

    place = place.merge(speed, how="left", left_on="FULLCODE", right_on="block_fips")
    #return place["max_speed"].groupby(["COUSUB"]).mean()
    return round(place["max_speed"].mean(),3)
    
def compute_avg():
    avg = compute_bb()
    print("\nMillinocket average download speed:", avg)

compute_avg()