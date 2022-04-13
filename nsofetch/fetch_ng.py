import pandas 
import numpy

import filepaths
import utils

def fetch_ng_inflation_cpi():
    stats_metadata = utils.read_stats_metadata()
    url = stats_metadata['NG']['inflation']['CPI']['url']
    tmp_filepath = utils.download_file(url)

    df = pandas.read_excel(tmp_filepath, sheet_name='Table1', header=None)
    df = df[17:331]
    output_df = pandas.DataFrame({'year': df.iloc[:, 0], 'month': df.iloc[:, 1], 'observations': df.iloc[:, 5]})

    # there must be a simpler way to do this, anyway, it replaces empty years with their correct value
    clean_years = []
    last_year = 0
    for i in output_df.year.to_list():
        if type(i) == int:
            clean_years.append(i)
            last_year = i
        elif i is numpy.NaN:
            clean_years.append(last_year)
    output_df.year = clean_years

    # some months are 3-letter, others are full name – replace with number value
    month_map = {
        'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12', 
        'January': '01', 'February': '02', 'March': '03', 'April': '04', 'May': '05', 'June': '06', 'July': '07', 'August': '08', 'September': '09', 'October': '10', 'November': '11', 'December': '12',
    }
    output_df.month = output_df.month.map(month_map)

    output_filepath = filepaths.DATA_DIR / stats_metadata['NG']['inflation']['CPI']['filename']
    output_df.to_csv(output_filepath, index=False)

if __name__ == '__main__':
    fetch_ng_inflation_cpi()
