import json
import csv

import requests

import filepaths
import utils


def month_name_to_num(month_name):
    month_map = {
        'January': '01', 'February': '02', 'March': '03', 'April': '04', 'May': '05', 'June': '06', 
        'July': '07', 'August': '08', 'September': '09', 'October': '10', 'November': '11', 'December': '12',
    }
    return month_map[month_name]


def fetch_uk_stat(url: str, output_filepath: str):
    response = requests.get(url)
    stats = json.loads(response.text)

    csv_output = [['month', 'observation']]
    for stat in stats['months']:
        month_val = stat['year'] + '-' + month_name_to_num(stat['month'])
        csv_output.append([month_val, stat['value']])

    with open(output_filepath, "w") as file:
        writer = csv.writer(file)
        writer.writerows(csv_output)


def fetch_uk_inflation_cpi():
    stats_metadata = utils.read_stats_metadata()
    url = stats_metadata['UK']['inflation']['CPI']['url']
    output_filepath = filepaths.DATA_DIR / stats_metadata['UK']['inflation']['CPI']['filename']
    fetch_uk_stat(url, output_filepath)


def fetch_uk_inflation_cpih():
    stats_metadata = utils.read_stats_metadata()
    url = stats_metadata['UK']['inflation']['CPIH']['url']
    output_filepath = filepaths.DATA_DIR / stats_metadata['UK']['inflation']['CPIH']['filename']
    fetch_uk_stat(url, output_filepath)


def fetch_uk_inflation_rpi():
    stats_metadata = utils.read_stats_metadata()
    url = stats_metadata['UK']['inflation']['RPI']['url']
    output_filepath = filepaths.DATA_DIR / stats_metadata['UK']['inflation']['RPI']['filename']
    fetch_uk_stat(url, output_filepath)


if __name__ == '__main__':
    fetch_uk_inflation_cpi()
    fetch_uk_inflation_cpih()
    fetch_uk_inflation_rpi()