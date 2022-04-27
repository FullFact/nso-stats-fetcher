import pandas
import matplotlib
import hvplot
import hvplot.pandas # noqa


import utils 
import filepaths


def plot_inflation_stats():
    stats_metadata = utils.read_stats_metadata()

    input_filepath = filepaths.DATA_DIR / stats_metadata['AR']['inflation']['CPI']['filename']
    df_ar_inflation = pandas.read_csv(input_filepath, index_col=0, parse_dates=['month'], infer_datetime_format=True)

    input_filepath = filepaths.DATA_DIR / stats_metadata['UK']['inflation']['CPI']['filename']
    df_uk_inflation = pandas.read_csv(input_filepath, index_col=0, parse_dates=['month'], infer_datetime_format=True)

    input_filepath = filepaths.DATA_DIR / stats_metadata['NG']['inflation']['CPI']['filename']
    df_ng_inflation = pandas.read_csv(input_filepath, index_col=0, parse_dates=['month'], infer_datetime_format=True)

    input_filepath = filepaths.DATA_DIR / stats_metadata['ZA']['inflation']['CPI']['filename']
    df_za_inflation = pandas.read_csv(input_filepath, index_col=0, parse_dates=['month'], infer_datetime_format=True)

    # fix this so that it's a combination of all the indexes
    idx = df_za_inflation.index

    df_plot = pandas.DataFrame(
        {
            'Argentina': df_ar_inflation.observation, 
            'Nigeria': df_ng_inflation.observation, 
            'UK': df_uk_inflation.observation, 
            'South Africa': df_za_inflation.observation
        }, 
        index=idx
    )

    output_filepath = filepaths.DATA_DIR / 'inflation_stats.html'
    plot = df_plot.hvplot(y=['Argentina', 'Nigeria', 'UK', 'South Africa'], value_label='Yearly inflation % (CPI)', legend='top', height=500, width=620)
    hvplot.save(plot, output_filepath)


if __name__ == '__main__':
    plot_inflation_stats()
