# Allows use of make data while having a data folder
.PHONY: data

# Creates the data folder and populates it with the necessary files
data:
	mkdir -p data
	cd data; curl -LO https://www2.census.gov/geo/tiger/TIGER2019/TRACT/tl_2019_23_tract.zip
	cd data; curl -LO https://www2.census.gov/programs-surveys/demo/datasets/community-resilience/county_tract_total_covered_populations.xlsx
	python -B src/make_dictionary.py
	python -B src/make_county_dictionary.py
	python -B src/create_json.py
	python -B src/create_county_json.py

plots:
	mkdir -p figs
	mkdir -p figs/tract
	mkdir -p figs/county
	python -B src/make_plots.py
	python -B src/make_county_plots.py

# Removes the data folder and all of its contents
clean: 
	rm -rf data
