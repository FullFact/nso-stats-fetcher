import csv
import itertools

from numpy import NaN 
import tabula
import pandas

import filepaths
import utils

MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

def fetch_za_inflation_cpi():
    stats_metadata = utils.read_stats_metadata()

    url = stats_metadata['ZA']['inflation']['CPI']['url']
    tables = tabula.read_pdf(url, pages="all", multiple_tables=True)

    # tables are split between two PDF pages
    df = pandas.concat([tables[1], tables[2]])
    # first 10 years only have yearly average inflation rate
    df.drop(df.index[:11], inplace=True)
    df.reset_index()

    years = list(itertools.chain(*[[i]*12 for i in df.Year.tolist()]))
    months = [f"{i:02}" for i in range(1, 13)] * len(df.Year)

    from locale import atof, setlocale, LC_NUMERIC
    setlocale(LC_NUMERIC, '')

    observations = []
    for row in df.iterrows():
        observations += row[1]['Jan':'Dec'].tolist()

    output_df = pandas.DataFrame({'year': years, 'month': months, 'observations': observations})
    output_df.dropna(inplace=True)
    output_df.observations = output_df.observations.str.replace(',', '.')

    output_filepath = filepaths.DATA_DIR / stats_metadata['ZA']['inflation']['CPI']['filename']
    output_df.to_csv(output_filepath, index=False)


def fetch_za_inflation_ppi():
    stats_metadata = utils.read_stats_metadata()

    url = stats_metadata['ZA']['inflation']['CPI']['url']
    tables = tabula.read_pdf(url, pages="all", multiple_tables=False)

    # tables are split between two PDF pages
    za_ppi_df = tables[0]
    # drop Average column 
    za_ppi_df.drop('Average', axis=1, inplace=True)
    # this PDF table is so awkward I can't see a way to get data without hardcoding
    years = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
    table_row_inds = [4, 6, 8, 10, 12, 14, 16, 18, 20, 24]
    table_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    csv_data = [['year', 'month', 'observation']]
    for row_ind, year in zip(table_row_inds, years):
        for month_ind, month in enumerate(table_months):
            # table cell value
            val = za_ppi_df.at[row_ind, table_months[month_ind]]
            # ignore blank values
            if val == '..': continue
            val = float(val.replace(',', '.'))
            csv_data.append([year, MONTHS[month_ind], val])

    output_filepath = filepaths.DATA_DIR / stats_metadata['ZA']['inflation']['PPI']['filename']
    with open(output_filepath, 'w') as csvfile: 
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(csv_data)



if __name__ == '__main__':
    fetch_za_inflation_cpi()
    # fetch_za_inflation_ppi()
