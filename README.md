# broadband-3

## Step 0
Run following command to download all of the data:
```
make data
```
The data comes from the following sources:

The FCC National Broadband Map [here](https://broadbandmap.fcc.gov/data-download/nationwide-data).  
Download the data for Cable, Copper, and Fiber to the Premises, then save those to your data folder.

The US Census Bureau shapefiles [here](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html).
The specific file is found [here](https://www2.census.gov/geo/tiger/TIGER2022/TABBLOCK20/tl_2022_23_tabblock20.zip).

US Census Bureau county subdivision information [here](https://www2.census.gov/geo/maps/DC2020/DC20BLK/st23_me/cousub/cs2301945810_millinocket/DC20BLK_CS2301945810_BLK2MS.txt).


## Step 1
Run the following command to a csv file with the maximum download speeds for Cable, Copper, and Fiber for each census block in Maine:

```
make speed
```

## Step 2
Calculate the average download speeed for Millinocket, which will be printed to the terminal.
```
make avg
```