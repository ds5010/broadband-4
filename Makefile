# Allows use of `make data` while having a data folder
.PHONY: data

# Creates and populates the data folder
data:
	mkdir -p data
	cd data; curl -LO https://www2.census.gov/geo/tiger/TIGER2019/TRACT/tl_2019_23_tract.zip
	cd data; curl -LO https://www2.census.gov/geo/tiger/TIGER2019/COUNTY/tl_2019_us_county.zip
	cd data; curl -LO https://www2.census.gov/programs-surveys/demo/datasets/community-resilience/county_tract_total_covered_populations.xlsx

clean:
	rm -rf data
