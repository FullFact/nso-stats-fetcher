import numpy
import pandas 

import utils
import filepaths

def fetch_jp_inflation_cpi():
    stats_metadata = utils.read_stats_metadata()
    url = stats_metadata['JP']['inflation']['CPI']['url']

    tmp_filepath = utils.download_file(url)

    df = pandas.read_excel(tmp_filepath, sheet_name='am01-1 (3)', header=None)
    # first bunch of rows have no info
    df.drop(df.loc[0:df.index[df[7] == '1971年 1月'][0]-1].index, inplace=True)
    # last bunch of rows also have no info
    df = df[~df[7].isnull()]

    # really annoying formatting for dates - have to go through this rigamarole 
    times = []
    for month_unclean in df[7].tolist():
        if len(month_unclean.strip()) > 4:
            month_clean = month_unclean[:4] + '-' + '01'
            last_year = month_clean[:4]
        else:
            month_int = int(month_unclean.strip())
            month_clean = last_year + '-' + f"{month_int:02}"
        times.append(month_clean)

    observations = df[8].tolist()

    output_df = pandas.DataFrame({'month': times, 'observation': observations})
    output_filepath = filepaths.DATA_DIR / stats_metadata['JP']['inflation']['CPI']['filename']
    output_df.to_csv(output_filepath, index=False)


if __name__ == '__main__':
    fetch_jp_inflation_cpi()
