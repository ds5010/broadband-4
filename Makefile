# Allows use of make data while having a data folder
.PHONY: data

# Creates the data folder
data:
	mkdir -p data
	cd data; curl -LO https://raw.githubusercontent.com/ds5110/rdata/main/fcc/bdc_23_Cable_fixed_broadband_063022.zip
	cd data; curl -LO https://raw.githubusercontent.com/ds5110/rdata/main/fcc/bdc_23_Copper_fixed_broadband_063022.zip
	cd data; curl -LO https://raw.githubusercontent.com/ds5110/rdata/main/fcc/bdc_23_Fiber-to-the-Premises_fixed_broadband_063022.zip
	cd data; curl -LO https://www2.census.gov/geo/tiger/TIGER2022/TABBLOCK20/tl_2022_23_tabblock20.zip
	cd data; curl -LO https://www2.census.gov/geo/maps/DC2020/DC20BLK/st23_me/cousub/cs2301945810_millinocket/DC20BLK_CS2301945810_BLK2MS.txt


speed:
	python3 -B src/speeds.py

clean-data:
	rm -rf data




	
