import pandas 

import utils

def fetch_jp_inflation_cpi():
    stats_metadata = utils.read_stats_metadata()
    url = stats_metadata['JP']['inflation']['CPI']['url']

    tmp_filepath = utils.download_file(url)

    df = pandas.read_excel(tmp_filepath, sheet_name='am01-1 (3)', header=None)



if __name__ == '__main__':
    fetch_jp_inflation_cpi()
