from datetime import datetime
import json

import requests
import pandas

import filepaths

def fetch_uk_cpih():
    with open(filepaths.NSO_STATS_METADATA) as json_file:
        stats_metadata = json.load(json_file)

    # download spreadsheet from URL and save to tmp file, then read in
    url = stats_metadata['UK']['inflation']['CPIH']['url']
    r = requests.get(url)
    tmp_filepath = '/tmp/temp.xls'
    open(tmp_filepath, 'wb').write(r.content)

    custom_date_parser = lambda x: datetime.strptime(x, "%Y %b")
    xl = pandas.ExcelFile(tmp_filepath)
    # skip first 173 rows to get month data, and special formatting for dates
    df = xl.parse("data", header=None, names=['date', 'observation'], skiprows=173, parse_dates=['date'], date_parser=custom_date_parser)

    output_df = pandas.DataFrame(
        {'year': df['date'].dt.year, 
        'month': df['date'].dt.strftime('%b'), 
        'observation': df['observation']}
    ).copy()
    output_filepath = filepaths.DATA_DIR / stats_metadata['UK']['inflation']['CPIH']['filename']
    output_df.to_csv(output_filepath, index=False)


if __name__ == '__main__':
    fetch_uk_cpih()
