# Allows use of make data while having a data folder
.PHONY: data

# Creates the data folder and populates it with the necessary files
data:
	mkdir -p data
<<<<<<< HEAD
	cd data; curl -LO https://www2.census.gov/geo/tiger/GENZ2019/shp/cb_2019_us_county_500k.zip
	cd data; curl -LO https://www2.census.gov/geo/tiger/TIGER2019/TRACT/tl_2019_23_tract.zip
	cd data; curl -LO https://www2.census.gov/programs-surveys/demo/datasets/community-resilience/county_tract_total_covered_populations.xlsx

clean-data:
=======
	cd data; curl -LO https://www2.census.gov/geo/tiger/TIGER2019/TRACT/tl_2019_23_tract.zip
	cd data; curl -LO https://www2.census.gov/programs-surveys/demo/datasets/community-resilience/county_tract_total_covered_populations.xlsx

# Removes the data folder and all of its contents
clean: 
>>>>>>> fae1a8c1ea65e66cfe68c31c4e5b475830971cc0
	rm -rf data

