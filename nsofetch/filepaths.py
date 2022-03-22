from pathlib import Path
import os

ROOT_DIR = Path(os.path.realpath(os.path.join(os.path.dirname(__file__), '..')))

ZA_INFLATION_CPI_DATA = ROOT_DIR / 'data' / 'za_inflation_cpi.csv'
ZA_INFLATION_CPI_INFO = ROOT_DIR / 'data' / 'za_inflation_cpi.json'
