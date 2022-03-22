import json
import csv
from numpy import NaN 

import tabula
import pandas

import filepaths

def fetch_za_inflation_cpi():
    with open(filepaths.ZA_INFLATION_CPI_INFO) as json_file:
        stats_metadata = json.load(json_file)
    tables = tabula.read_pdf(stats_metadata['url'], pages="all", multiple_tables=True)

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
    months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
    za_cpi_lists = list(za_cpi_df.itertuples(index=False, name=None))

    for year, za_cpi_row in zip(years, za_cpi_lists):
        nums_rows = [
            [year, months[i], float(val.replace(',', '.'))] 
            for i, val in enumerate(za_cpi_row)
            # NaN checks if the cells are empty in the table 
            if val is not NaN
        ]
        csv_data += nums_rows

    with open(filepaths.ZA_INFLATION_CPI_DATA, 'w') as csvfile: 
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(csv_data)
        

if __name__ == '__main__':
    fetch_za_inflation_cpi()
