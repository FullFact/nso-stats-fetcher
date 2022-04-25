from datetime import datetime

import fetch_ar
import fetch_uk
import fetch_za

def add_last_updated():
    # just to keep all server times aligned, stick with UTC time everywhere
    utc_now = datetime.utcnow()
    dt_string = utc_now.strftime("%Y-%m-%d %H:%M:%S")

    out_str = "Last updated: " + dt_string + "\n"
    with open('status.txt', 'w') as the_file:
        the_file.write(out_str)

if __name__ == '__main__':
    print('getting uk data...')
    fetch_uk.fetch_uk_inflation_cpi()
    fetch_uk.fetch_uk_inflation_cpih()
    fetch_uk.fetch_uk_inflation_rpi()

    print('getting argentina data...')
    fetch_ar.fetch_ar_inflation_cpi()

    print('getting south africa data...')
    fetch_za.fetch_za_inflation_cpi()
    fetch_za.fetch_za_inflation_ppi()

    add_last_updated()

    print('done')