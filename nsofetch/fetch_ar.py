import pandas

import utils
import filepaths

def fetch_ar_inflation():
    stats_metadata = utils.read_stats_metadata()

    url = stats_metadata['AR']['inflation']['CPI']['url']
    tmp_filepath = utils.download_file(url)

    df = pandas.read_csv(tmp_filepath, parse_dates=['indice_tiempo'])
    output_df = pandas.DataFrame(
        {'year': df['indice_tiempo'].dt.year, 'month': df['indice_tiempo'].dt.strftime('%m'), 
        'observation': df['ipc_nivel_general_nacional_var_pct_ia']}).copy()
    
    output_df.observation = output_df.observation.apply(lambda x: x*100)

    output_filepath = filepaths.DATA_DIR / stats_metadata['AR']['inflation']['CPI']['filename']
    output_df.to_csv(output_filepath, index=False)


if __name__ == '__main__':
    fetch_ar_inflation()
