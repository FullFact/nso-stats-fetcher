import pandas

import utils
import filepaths

def fetch_ar_inflation():
    stats_metadata = utils.read_stats_metadata()

    url = stats_metadata['AR']['inflation']['url']
    tmp_filepath = utils.download_csv(url)

    df = pandas.read_csv(tmp_filepath, parse_dates=['indice_tiempo'])
    output_df = pandas.DataFrame(
        {'year': df['indice_tiempo'].dt.year, 'month': df['indice_tiempo'].dt.strftime('%m'), 
        'observation': df['expectativa_inflacion_promedio']}).copy()
    
    output_filepath = filepaths.DATA_DIR / stats_metadata['AR']['inflation']['filename']
    output_df.to_csv(output_filepath, index=False)


if __name__ == '__main__':
    fetch_ar_inflation()
