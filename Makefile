# Allows use of make data while having a data folder
.PHONY: data

# Creates the data folder and populates it with the necessary files
data:
	mkdir -p data
	mkdir -p docs
	python -B src/get_DE_csv.py
	python -B src/get_shapefile.py
	python -B src/make_jsons.py

density:
	python -B src/plot_density.py

plots:
	python -B src/make_plots.py

# Removes the data folder and all of its contents
clean: 
	rm -rf data

