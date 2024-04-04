.PHONY: data

# Creates the data folder and populates it with the necessary files
data: 
	mkdir -p data
	cd data; curl -O https://www2.census.gov/geo/tiger/TIGER2019/TRACT/tl_2019_23_tract.zip
	cd data; curl -O https://www2.census.gov/programs-surveys/demo/datasets/community-resilience/county_tract_total_covered_populations.xlsx


# Creates the json file in the data directory from the desired data contained in the zip and xlsx files	
json: 
	python -B src/create_json.py
	
# Removes the data folder and all of its contents
clean: 
	rm -rf data