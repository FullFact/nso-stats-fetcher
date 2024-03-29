import sys
import itertools

import tabula
import pandas
import numpy

import filepaths
import utils


def fetch_za_inflation_cpi():
    stats_metadata = utils.read_stats_metadata()

    url = stats_metadata["ZA"]["inflation"]["CPI"]["url"]
    try:
        tables = tabula.read_pdf(url, pages="all", multiple_tables=True)
    except:
        print("Failed to parse PDF tables; aborting")
        return

    # tables are split between two PDF pages
    df = pandas.concat([tables[1], tables[2]], ignore_index=True)
    # first 10 years only have yearly average inflation rate
    df.drop(df.index[:11], inplace=True)
    df.reset_index()

    # need to create a list with 12 repeats of each year
    years = list(itertools.chain(*[[i] * 12 for i in df.Year.tolist()]))
    months = [f"{i:02}" for i in range(1, 13)] * len(df.Year)
    times = [str(year) + "-" + str(month) for year, month in zip(years, months)]

    observations = []
    for row in df.iterrows():
        observations += row[1]["Jan":"Dec"].tolist()

    output_df = pandas.DataFrame({"month": times, "observation": observations})
    output_df.dropna(inplace=True)
    # convert from ZA format of commas for decimal places to dots
    output_df.observation = output_df.observation.str.replace(",", ".")

    output_filepath = (
        filepaths.DATA_DIR / stats_metadata["ZA"]["inflation"]["CPI"]["filename"]
    )
    output_df.to_csv(output_filepath, index=False)


def fetch_za_inflation_ppi():
    stats_metadata = utils.read_stats_metadata()

    url = stats_metadata["ZA"]["inflation"]["PPI"]["url"]
    try:
        tables = tabula.read_pdf(url, pages="all", multiple_tables=False)
    except:
        print("Failed to parse PDF tables; aborting")
        return

    df = tables[0]

    # very awkward year column to read
    years = [
        a.replace(" Index", "")
        for a in df["Year and"].tolist()
        if a not in ["type", "Rate", "Index", numpy.nan]
    ]
    months = [f"{i:02}" for i in range(1, 13)] * len(years)
    years = list(
        itertools.chain(*[[i] * 12 for i in years])
    )  # flatten the list of lists of years
    times = [str(year) + "-" + str(month) for year, month in zip(years, months)]

    observations = []
    for row_tuple in df.itertuples():
        if row_tuple._1 != "Rate":
            continue
        observations += [
            row_tuple.Jan,
            row_tuple.Feb,
            row_tuple.Mar,
            row_tuple.Apr,
            row_tuple.May,
            row_tuple.Jun,
            row_tuple.Jul,
            row_tuple.Aug,
            row_tuple.Sep,
            row_tuple.Oct,
            row_tuple.Nov,
            row_tuple.Dec,
        ]

    output_df = pandas.DataFrame({"month": times, "observation": observations})
    # this PDF table marks missing values with '..' - so drop those
    output_df = output_df[output_df.observation != ".."]
    # convert from ZA format of commas for decimal places to dots
    output_df.observation = output_df.observation.str.replace(",", ".")

    output_filepath = (
        filepaths.DATA_DIR / stats_metadata["ZA"]["inflation"]["PPI"]["filename"]
    )
    output_df.to_csv(output_filepath, index=False)


if __name__ == "__main__":
    scraper_to_run = sys.argv[1] if len(sys.argv) > 1 else "-"
    if scraper_to_run in ["cpi", "-"]:
        fetch_za_inflation_cpi()
    if scraper_to_run in ["ppi", "-"]:
        fetch_za_inflation_ppi()
