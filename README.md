# Broadband-4
This repository takes data about Maine populations and plots them based on census tracts and counties.

## Instructions for Use
### *Step 1: Generating the Data*
After cloning the repository, the following command will download and clean necessary data, placing them within the required directories
```
make data
```

### *Step 2: Reproducing the Map Figures*
The following command will plot the figures of covered populations of Maine tracts/counties based on numerous factors and save the PNGs in the `figs` directory. The covered population factors include *Total Covered Households, Low Income/Poverty, Ages 60+, Incarcerated, Disability, Veterans, Language Barrier, Those w/o Broadband or Computers, Minorities, Rural Living, ESL, Low Literacy (county only), and Those w/o Fixed Broadband (county only)*.
```
make plots
```
### Tract Plots
<p align="center">
    <img src="figs/tract/covered_population.png" width="700">
</p><br>

<p align="center">
    <img src="figs/tract/near_poverty.png" width="700">
</p><br>

<p align="center">
    <img src="figs/tract/Age 60+.png" width="700">
</p><br>

<p align="center">
    <img src="figs/tract/Incarcerated.png" width="700">
</p><br>

<p align="center">
    <img src="figs/tract/Disabled.png" width="700">
</p><br>

<p align="center">
    <img src="figs/tract/Veterans.png" width="700">
</p><br>

<p align="center">
    <img src="figs/tract/Language Barrier.png" width="700">
</p><br>

<p align="center">
    <img src="figs/tract/Lack Broadband or Computers.png" width="700">
</p><br>

<p align="center">
    <img src="figs/tract/Minorities.png" width="700">
</p><br>

<p align="center">
    <img src="figs/tract/People in Rural Areas.png" width="700">
</p><br>

<p align="center">
    <img src="figs/tract/Non-native English Speakers.png" width="700">
</p><br>

### County Plots
<p align="center">
    <img src="figs/county/covered_population.png" width="700">
</p><br>

<p align="center">
    <img src="figs/county/near_poverty.png" width="700">
</p><br>

<p align="center">
    <img src="figs/county/Age 60+.png" width="700">
</p><br>

<p align="center">
    <img src="figs/county/Incarcerated.png" width="700">
</p><br>

<p align="center">
    <img src="figs/county/Disabled.png" width="700">
</p><br>

<p align="center">
    <img src="figs/county/Veterans.png" width="700">
</p><br>

<p align="center">
    <img src="figs/county/Language Barrier.png" width="700">
</p><br>

<p align="center">
    <img src="figs/county/Lack Broadband or Computers.png" width="700">
</p><br>

<p align="center">
    <img src="figs/county/Minorities.png" width="700">
</p><br>

<p align="center">
    <img src="figs/county/People in Rural Areas.png" width="700">
</p><br>

<p align="center">
    <img src="figs/county/Non-native English Speakers.png" width="700">
</p><br>

<p align="center">
    <img src="figs/county/County-level Only Columns.png" width="700">
</p><br>
