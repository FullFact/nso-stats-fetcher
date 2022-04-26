import pandas
import numpy

import utils 
import filepaths


def plot_inflation_stats():
    stats_metadata = utils.read_stats_metadata()

    input_filepath = filepaths.DATA_DIR / stats_metadata['UK']['inflation']['CPI']['filename']
    df_uk_inflation = pandas.read_csv(input_filepath)

    input_filepath = filepaths.DATA_DIR / stats_metadata['AR']['inflation']['CPI']['filename']
    df_ar_inflation = pandas.read_csv(input_filepath)

    start_time = str(df_uk_inflation.iloc[0]['year']) + '-' + df_uk_inflation.iloc[0]['month']
    end_time = df_uk_inflation.iloc[-1]['year'] + '-' + df_uk_inflation.iloc[-1]['month']

    idx = pandas.date_range(start=start_time, end=end_time, freq='M')
    observations = numpy.arary([df_ar_inflation.observation, df_uk_inflation.obervation])
    columns = ['Argentina', 'UK']
    df  = pandas.DataFrame(observations, index=idx, columns=columns)

    # import hvplot.pandas  # noqa
    # df.hvplot()


if __name__ == '__main__':
    plot_inflation_stats()
