import pandas
import matplotlib
import hvplot
import hvplot.pandas # noqa


import utils 
import filepaths


def plot_inflation_stats():
    stats_metadata = utils.read_stats_metadata()

    input_filepath = filepaths.DATA_DIR / stats_metadata['UK']['inflation']['CPI']['filename']
    df_uk_inflation = pandas.read_csv(input_filepath, index_col=0)

    input_filepath = filepaths.DATA_DIR / stats_metadata['AR']['inflation']['CPI']['filename']
    df_ar_inflation = pandas.read_csv(input_filepath, index_col=0)

    start = df_uk_inflation.index[0]
    end = df_uk_inflation.index[-1]

    # fix this so that it's a combination of all the indexes
    idx = df_uk_inflation.index

    df_plot = pandas.DataFrame({'Argentina': df_ar_inflation.observation, 'UK': df_uk_inflation.observation}, index=idx)

    output_filepath = filepaths.DATA_DIR / 'inflation_stats.html'
    plot = df_plot.hvplot(y=['Argentina', 'UK'], value_label='Yearly inflation % (CPI)', legend='top', height=500, width=620)
    hvplot.save(plot, output_filepath)


if __name__ == '__main__':
    plot_inflation_stats()
