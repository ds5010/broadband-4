# Allows use of make data while having a data folder
.PHONY: data img

all: clean-data data img speed avg json state block DDI
# Creates the data folder
data:
	mkdir -p data
	cd data; curl -LO https://www2.census.gov/geo/tiger/GENZ2019/shp/cb_2019_us_county_500k.zip
	cd data; curl -LO https://www2.census.gov/geo/tiger/TIGER2019/TRACT/tl_2019_23_tract.zip
	cd data; curl -LO https://www2.census.gov/programs-surveys/demo/datasets/community-resilience/county_tract_total_covered_populations.xlsx

clean-data:
	rm -rf data

