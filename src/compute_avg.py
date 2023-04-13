import pandas as pd

millinocket = "data/DC20BLK_CS2301945810_BLK2MS.txt"


def compute_bb():
    ''' selects speeds for millinocket blocks and calculates average of those blocks
        returns: average (float)
    '''
    
    place = pd.read_csv(millinocket, sep=";")
    speed = pd.read_csv("data/speeds.csv")

    place = place.merge(speed, how="left", left_on="FULLCODE", right_on="block_fips")
    return round(place["max_speed"].mean(),3) #NAs are excluded from calculation


def compute_avg():
    avg = compute_bb()
    print("\nMillinocket average download speed:", avg)


if __name__ == "__main__":
    compute_avg()