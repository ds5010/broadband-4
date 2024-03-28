import covered_pop
import geopandas as gpd
import matplotlib.pyplot as plt


def covered_pop_plot(gdf, column, title):
    """
    Plots based on column and gives a title
    :param gdf: geodataframe to plot
    :param column: column from gdf to plot
    :param title: title of plot
    :return: None
    """
    ax = gdf.plot(column=column, legend=True)
    gdf.boundary.plot(ax=ax, linewidth=0.2, edgecolor='#ccc')
    ax.set_title(title)
    plt.savefig(f'figures/{column}.png')


def main():
    tract_df = covered_pop.cleaned_df()
    gdf = gpd.read_file("data/tl_2022_23_tract.zip")
    gdf["GEOID"] = gdf["GEOID"].astype("int64")
    combined_gdf = gdf.merge(tract_df, left_on="GEOID", right_on="geo_id")
    covered_pop_plot(combined_gdf, "pct_ipr_pop", 'Covered Households Percentage')
    covered_pop_plot(combined_gdf, "pct_aging_pop", '60 years and older')
    covered_pop_plot(combined_gdf, "pct_incarc_pop", 'Incarcerated')
    covered_pop_plot(combined_gdf, "pct_vet_pop", 'Veterans')
    covered_pop_plot(combined_gdf, "pct_dis_pop", 'Disabilities')
    covered_pop_plot(combined_gdf, "pct_lang_barrier_pop", 'Language Barrier')
    covered_pop_plot(combined_gdf, "pct_lang_pop", 'ESL')
    covered_pop_plot(combined_gdf, "pct_minority_pop", 'Minority Populations')
    covered_pop_plot(combined_gdf, "pct_rural_pop", 'Rural Living')
    covered_pop_plot(combined_gdf, "pct_no_bb_or_computer_pop", 'No Broadband and/or Computing Device')


if __name__ == "__main__":
    main()
