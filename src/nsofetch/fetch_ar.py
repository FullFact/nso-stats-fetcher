import os
import pandas
import requests

import utils
import filepaths


def fetch_ar_inflation_cpi():
    stats_metadata = utils.read_stats_metadata()

    proxies = {
        "http": os.environ["PROXY_URL"],
        "https": os.environ["PROXY_URL"],
    }
    url = stats_metadata["AR"]["inflation"]["CPI"]["url"]
    response = requests.get(url, proxies=proxies)
    response.raise_for_status()
    stats = response.json()

    months = []
    observations = []
    for row in stats["data"]:
        # drop the day number from data: eg. '2020-01-01' becomes '2020-01'
        months.append(row[0][:7])
        # convert decimal to percentage
        observations.append(row[1] * 100)

    output_df = pandas.DataFrame({"month": months, "observation": observations})
    output_filepath = (
        filepaths.DATA_DIR / stats_metadata["AR"]["inflation"]["CPI"]["filename"]
    )
    output_df.to_csv(output_filepath, index=False)


if __name__ == "__main__":
    fetch_ar_inflation_cpi()
