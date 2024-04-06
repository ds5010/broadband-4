# Broadband-4
This repository takes data about Maine populations and plots them based on census tracts.

## Instructions for Use
### *Step 1: Generating the Data*
After cloning the repository, the following command will download and clean necessary data, placing them within the required directories
```
make data
```

### *Step 2: Reproducing the Map Figures*
The following command will plot the figures of covered populations of Maine based on numerous factors and save the PNGs in the `figs` directory. The covered population factors include *Total Covered Households, Low Income/Poverty, Ages 60+, Incarcerated, Disability, Veterans, Language Barrier, Those w/o Broadband or Computers, Minorities, Rural Living, and ESL*.
```
make plots
```
<p align="center">
    <img src="figs/covered_population.png" width="700">
</p><br>

<p align="center">
    <img src="figs/near_poverty.png" width="700">
</p><br>

<p align="center">
    <img src="figs/Age 60+.png" width="700">
</p><br>

<p align="center">
    <img src="figs/Incarcerated.png" width="700">
</p><br>

<p align="center">
    <img src="figs/Disabled.png" width="700">
</p><br>

<p align="center">
    <img src="figs/Veterans.png" width="700">
</p><br>

<p align="center">
    <img src="figs/Language Barrier.png" width="700">
</p><br>

<p align="center">
    <img src="figs/Lack Broadband or Computers.png" width="700">
</p><br>

<p align="center">
    <img src="figs/Minorities.png" width="700">
</p><br>

<p align="center">
    <img src="figs/People in Rural Areas.png" width="700">
</p><br>

<p align="center">
    <img src="figs/Non-native English Speakers.png" width="700">
</p><br>