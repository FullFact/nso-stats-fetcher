import pandas

import filepaths
import utils


def fetch_mx_inflation_cpi():

    stats_metadata = utils.read_stats_metadata()
    url = stats_metadata['MX']['inflation']['CPI']['url']

    tmp_filepath = utils.download_file(url)
    df = pandas.read_excel(tmp_filepath, sheet_name='Sheet 1', header=None)

    # first few rows are blank, so skip until the row with 1970
    df.drop(df.loc[0:df.index[df[0] == '1970/01'][0]-1].index, inplace=True)
    df.reset_index(drop=True, inplace=True)

    # last few don't have useful info, so drop them
    df.drop(df.index[df.loc[pandas.isna(df[0]), :].index[0]:], inplace=True)

    df.columns = ['month', 'observation']

    # reformat month from 1970/01 to standard format of 1970-01
    df['month'] = df['month'].str.replace('/','-')

    output_filepath = filepaths.DATA_DIR / stats_metadata['MX']['inflation']['CPI']['filename']
    df.to_csv(output_filepath, index=False)


if __name__ == '__main__':
    fetch_mx_inflation_cpi()
