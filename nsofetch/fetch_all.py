import fetch_ar
import fetch_ng
import fetch_uk
import fetch_za

print('getting argentina data...')
fetch_ar.fetch_ar_inflation_cpi()

print('getting nigeria data...')
fetch_ng.fetch_ng_inflation_cpi()

print('getting uk data...')
fetch_uk.fetch_uk_inflation_cpi()
fetch_uk.fetch_uk_inflation_cpih()
fetch_uk.fetch_uk_inflation_rpi()

print('getting south africa data...')
fetch_za.fetch_za_inflation_cpi()
fetch_za.fetch_za_inflation_ppi()
