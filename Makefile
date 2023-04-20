# Allows use of make data while having a data folder
.PHONY: data img

# Creates the data folder
data:
	mkdir -p data
	cd data; curl -LO https://www2.census.gov/geo/tiger/TIGER2022/TABBLOCK20/tl_2022_23_tabblock20.zip
	cd data; curl -LO https://www2.census.gov/geo/maps/DC2020/DC20BLK/st23_me/cousub/cs2301945810_millinocket/DC20BLK_CS2301945810_BLK2MS.txt
	cd data; curl -LO https://github.com/dobnu/fcc-data/raw/main/bdc_23_Cable_fixed_broadband_063022.zip
	cd data; curl -LO https://github.com/dobnu/fcc-data/raw/main/bdc_23_Copper_fixed_broadband_063022.zip
	cd data; curl -LO https://github.com/dobnu/fcc-data/raw//main/bdc_23_Fiber-to-the-Premises_fixed_broadband_063022.zip
	cd data; curl -LO https://github.com/dobnu/fcc-data/raw/main/bdc_23_Licensed-Fixed-Wireless_fixed_broadband_063022.zip

img:
	mkdir -p img

speed:
	python3 -B src/speeds.py

avg:
	python3 -B src/compute_avg.py

json:
	python3 -B src/create_json.py

state: img
	python3 -B src/plot_state.py

block: img
	python3 -B src/plot_block.py

DDI: data/
	python3 -B src/DDI.py

maps: data/
	python3 -B src/maps.py

clean-data:
	rm -rf data
