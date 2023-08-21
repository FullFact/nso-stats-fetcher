import requests
import pandas

import filepaths
import utils


def fetch_ie_inflation_cpi():
    stats_metadata = utils.read_stats_metadata()
    url = stats_metadata['IE']['inflation']['CPI']['url']

    response = requests.get(url)
    response.raise_for_status()
    stats = response.json()

    months = stats['result']['dimension']['TLIST(M1)']['category']['index']
    months = [month[:4] + '-' + month[4:] for month in months]
    observations = stats['result']['value']

    output_df = pandas.DataFrame({'month': months, 'observation': observations})
    output_df.dropna(inplace=True)
    output_filepath = filepaths.DATA_DIR / stats_metadata['IE']['inflation']['CPI']['filename']
    output_df.to_csv(output_filepath, index=False)


if __name__ == '__main__':
    fetch_ie_inflation_cpi()
