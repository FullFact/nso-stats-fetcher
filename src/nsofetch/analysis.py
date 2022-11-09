import pandas
import hvplot
import hvplot.pandas # noqa


import utils 
import filepaths


def plot_inflation_stats():
    stats_metadata = utils.read_stats_metadata()

    input_filepath = filepaths.DATA_DIR / stats_metadata['AR']['inflation']['CPI']['filename']
    df_ar_inflation = pandas.read_csv(input_filepath, index_col=0, parse_dates=['month'], infer_datetime_format=True)

    input_filepath = filepaths.DATA_DIR / stats_metadata['IE']['inflation']['CPI']['filename']
    df_ie_inflation = pandas.read_csv(input_filepath, index_col=0, parse_dates=['month'], infer_datetime_format=True)

    input_filepath = filepaths.DATA_DIR / stats_metadata['JP']['inflation']['CPI']['filename']
    df_jp_inflation = pandas.read_csv(input_filepath, index_col=0, parse_dates=['month'], infer_datetime_format=True)

    input_filepath = filepaths.DATA_DIR / stats_metadata['MX']['inflation']['CPI']['filename']
    df_mx_inflation = pandas.read_csv(input_filepath, index_col=0, parse_dates=['month'], infer_datetime_format=True)

    input_filepath = filepaths.DATA_DIR / stats_metadata['NG']['inflation']['CPI']['filename']
    df_ng_inflation = pandas.read_csv(input_filepath, index_col=0, parse_dates=['month'], infer_datetime_format=True)

    input_filepath = filepaths.DATA_DIR / stats_metadata['PH']['inflation']['CPI']['filename']
    df_ph_inflation = pandas.read_csv(input_filepath, index_col=0, parse_dates=['month'], infer_datetime_format=True)

    input_filepath = filepaths.DATA_DIR / stats_metadata['UK']['inflation']['CPI']['filename']
    df_uk_inflation = pandas.read_csv(input_filepath, index_col=0, parse_dates=['month'], infer_datetime_format=True)

    input_filepath = filepaths.DATA_DIR / stats_metadata['ZA']['inflation']['CPI']['filename']
    df_za_inflation = pandas.read_csv(input_filepath, index_col=0, parse_dates=['month'], infer_datetime_format=True)

    # fix this so that it's a combination of all the indexes
    idx = df_za_inflation.index

    df_plot = pandas.DataFrame(
        {
            'Argentina': df_ar_inflation.observation, 
            'Ireland': df_ie_inflation.observation, 
            'Japan': df_jp_inflation.observation,
            'Mexico': df_mx_inflation.observation,
            'Nigeria': df_ng_inflation.observation, 
            'Philippines': df_ph_inflation.observation,
            'UK': df_uk_inflation.observation, 
            'South Africa': df_za_inflation.observation
        }, 
        index=idx
    )

    output_filepath = filepaths.DATA_DIR / 'inflation_stats.html'
    plot = df_plot.hvplot(
        y=['Argentina', 'Ireland', 'Japan', 'Mexico','Nigeria', 'Philippines', 'UK', 'South Africa'], 
        value_label='Yearly inflation % (CPI)', legend='top', height=700, width=1000
    )
    hvplot.save(plot, output_filepath)


if __name__ == '__main__':
    plot_inflation_stats()
