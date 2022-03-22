from pathlib import Path
import os

ROOT_DIR = Path(os.path.realpath(os.path.join(os.path.dirname(__file__), '..')))

# Statistics South Africa
ZA_INFLATION_CPI_DATA = ROOT_DIR / 'data' / 'za_inflation_cpi.csv'
ZA_INFLATION_CPI_INFO = ROOT_DIR / 'data' / 'za_inflation_cpi.json'
ZA_INFLATION_PPI_DATA = ROOT_DIR / 'data' / 'za_inflation_ppi.csv'
ZA_INFLATION_PPI_INFO = ROOT_DIR / 'data' / 'za_inflation_ppi.json'

# Office of National Statistics - United Kingdom 
UK_INFLATION_CPI_DATA = ROOT_DIR / 'data' / 'uk_inflation_cpi.csv'
UK_INFLATION_CPI_INFO = ROOT_DIR / 'data' / 'uk_inflation_cpi.json'
