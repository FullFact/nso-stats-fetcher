import requests
import pandas

import filepaths

import json

def fetch_uk_cpih():
    with open(filepaths.NSO_STATS_METADATA) as json_file:
        stats_metadata = json.load(json_file)

    # download spreadsheet from URL and save to tmp file, then read in
    url = stats_metadata['UK']['inflation']['CPIH']['url']
    r = requests.get(url)
    tmp_filepath = '/tmp/temp.xls'
    open(tmp_filepath, 'wb').write(r.content)

    # on Contents sheet: Table 57	CPI: Detailed indices to 3 dp: 1988-2022
    df = pandas.read_excel(tmp_filepath, sheet_name='data', skiprows=173)
    
    print('here')
    




if __name__ == '__main__':
    fetch_uk_cpih()
