# Allows use of make data while having a data folder
.PHONY: data img

all: clean-data data img speed avg json state block DDI
# Creates the data folder
data:
	mkdir -p data
	cd data; curl -LO https://www2.census.gov/geo/tiger/TIGER2022/TABBLOCK20/tl_2022_23_tabblock20.zip
	cd data; curl -LO https://www2.census.gov/geo/tiger/TIGER2019/TRACT/tl_2019_23_tract.zip

clean-data:
	rm -rf data

