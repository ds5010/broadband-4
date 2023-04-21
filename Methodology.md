# Our Methodology

## Purdue Digital Divide Index (DDI)

We started with the [Purdue Digital Divide Index](https://storymaps.arcgis.com/stories/8ad45c48ba5c43d8ad36240ff0ea0dc7), by attempting to compute their calculations using broadband speed data from the FCC, rather than Ookla Speedtest(R) results.

We used the maximum of download/upload max speeds offered by providers of broadband cable, copper, fiber, and licensed fixed wireless in each census sub-block. Then we averaged those for each census tract.

Like Purdue's, our population data came from the 2021 5 year American Community Survey.


### Calculation

INFA = NBBND*0.3 + NIA*0.3 + NCD*0.3 – DNS*0.05 – UPS*0.05
SE = AGE65 + POV + LTHS + DIS
DDI = INFA + SE

#### INFA (Infrastructure/adoption)
* NBBND : z-scores of the percent of population without fixed 100/20
* NIA: z-scores of the percent of population with no internet access
* NCD: z-scores of the percent of population with no computing devices (NCD)
* DNS: z-scores of the average max download available (DNS)
* UPS: z-scores of the average max upload available (UPS)

#### SE (Socioeconomic)
* AGE65: z-scores of the percent population ages 65 and over
* POV: z-scores of individual poverty rate
* LTHS: z-scores of percent population 25 and over without a high school degree
* DIS: z-scores of percent noninstutionalized population with any disability (DIS)


## Complications

* The FCC data we are using is what providers report they offer in a given location. It differs from the results of the Ookla tests that Purdue used. Consequently, our DDI results differ as well.

* We intended to compute DDI at the census block group level. Unfortunately, POV, LTHS and DIS were only available at the tract level, which is why we averaged the amounts there. There are 358 tracts in Maine, compared to 1,086 block groups.


## Resources

#### FCC Internet Speeds
* [FCC National Broadband Map](https://broadbandmap.fcc.gov/data-download/nationwide-data?version=jun2022)

#### Geography Data
* [Shapefiles from the US Census Bureau](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html)
* [The specific file that we used from the Census](https://www2.census.gov/geo/tiger/TIGER2022/TABBLOCK20/tl_2022_23_tabblock20.zip)

#### Purdue DDI Information
* [Purdue Digital Divide Index](https://storymaps.arcgis.com/stories/8ad45c48ba5c43d8ad36240ff0ea0dc7)
* [Purdue DDI Additional Info](https://pcrd.purdue.edu/ruralindianastats/broadband/ddi.php?variable=ddi-overview&county=Adams)

#### American Community Survey - 5 Year - 2021
* [ACS 5 Main Page](https://www.census.gov/data/developers/data-sets/acs-5year.html)