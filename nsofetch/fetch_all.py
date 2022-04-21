from datetime import datetime

import fetch_uk

def add_last_updated():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    readme = open("README.md", "r")
    list_of_lines = readme.readlines()
    list_of_lines[1] = "_Last updated: " + dt_string + "_\n\n"

    a_file = open("README.md", "w")
    a_file.writelines(list_of_lines)
    a_file.close()


if __name__ == '__main__':
    print('getting uk data...')
    fetch_uk.fetch_uk_inflation_cpi()
    fetch_uk.fetch_uk_inflation_cpih()
    fetch_uk.fetch_uk_inflation_rpi()

    add_last_updated()

    print('done')