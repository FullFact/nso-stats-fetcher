from datetime import datetime

import pandas

import filepaths
import utils

def fetch_uk_stat(url: str, skiprows: int, output_filepath: str):
    tmp_filepath = utils.download_csv(url)

    # skip first X rows to get month data, and special formatting for dates
    custom_date_parser = lambda x: datetime.strptime(x, "%Y %b")
    df = pandas.read_csv(tmp_filepath, skiprows=skiprows, header=None, names=['date', 'observation'], 
        parse_dates=['date'], date_parser=custom_date_parser)

    output_df = pandas.DataFrame(
        {'year': df['date'].dt.year, 
        'month': df['date'].dt.strftime('%b'), 
        'observation': df['observation']}
    ).copy()
    output_df.to_csv(output_filepath, index=False)

def fetch_uk_cpih():
    stats_metadata = utils.read_stats_metadata()
    skiprows = 173
    url = stats_metadata['UK']['inflation']['CPIH']['url']
    output_filepath = filepaths.DATA_DIR / stats_metadata['UK']['inflation']['CPIH']['filename']

    fetch_uk_stat(url, skiprows, output_filepath)

def fetch_uk_cpi():
    stats_metadata = utils.read_stats_metadata()
    url = stats_metadata['UK']['inflation']['CPIH']['url']
    skiprows = 173
    output_filepath = filepaths.DATA_DIR / stats_metadata['UK']['inflation']['CPI']['filename']
    
    fetch_uk_stat(url, skiprows, output_filepath)


def fetch_uk_rpi():
    stats_metadata = utils.read_stats_metadata()
    url = stats_metadata['UK']['inflation']['RPI']['url']
    skiprows = 375
    output_filepath = filepaths.DATA_DIR / stats_metadata['UK']['inflation']['RPI']['filename']
    
    fetch_uk_stat(url, skiprows, output_filepath)

if __name__ == '__main__':
    fetch_uk_cpih()
    fetch_uk_cpi()
    fetch_uk_rpi()