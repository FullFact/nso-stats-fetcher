from datetime import datetime

import fetch_uk

def add_last_updated():
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")

    out_str = "Last updated: " + dt_string + "\n"
    with open('status.txt', 'w') as the_file:
        the_file.write(out_str)

if __name__ == '__main__':
    print('getting uk data...')
    fetch_uk.fetch_uk_inflation_cpi()
    fetch_uk.fetch_uk_inflation_cpih()
    fetch_uk.fetch_uk_inflation_rpi()

    add_last_updated()

    print('done')