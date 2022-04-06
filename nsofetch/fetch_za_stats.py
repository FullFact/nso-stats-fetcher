import csv

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
    za_cpi_df = pandas.concat([tables[1], tables[2]])
    # first 10 years only have yearly average inflation rate
    za_cpi_df.drop(za_cpi_df.index[:11], inplace=True)
    # drop Average column 
    za_cpi_df.drop('Average', axis=1, inplace=True)
    # get list of years from first column then drop that column
    years = za_cpi_df.iloc[:, 0].tolist()
    za_cpi_df.drop(za_cpi_df.columns[0], axis=1, inplace=True)

    csv_data = [['year', 'month', 'observation']]
    za_cpi_lists = list(za_cpi_df.itertuples(index=False, name=None))

    for year, za_cpi_row in zip(years, za_cpi_lists):
        nums_rows = [
            [year, MONTHS[i], round(float(val.replace(',', '.')), 1)] 
            for i, val in enumerate(za_cpi_row)
            # NaN checks if the cells are empty in the table 
            if val is not NaN
        ]
        csv_data += nums_rows

    output_filepath = filepaths.DATA_DIR / stats_metadata['ZA']['inflation']['CPI']['filename']
    with open(output_filepath, 'w') as csvfile: 
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(csv_data)


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
    fetch_za_inflation_ppi()
