from pathlib import Path
import os

ROOT_DIR = Path(os.path.realpath(os.path.join(os.path.dirname(__file__), '..')))
DATA_DIR = ROOT_DIR / 'data'

NSO_STATS_METADATA = ROOT_DIR / 'data' / 'nso_stats_metadata.json'

# Statistics South Africa
ZA_INFLATION_CPI_DATA = ROOT_DIR / 'data' / 'za_inflation_cpi.csv'
ZA_INFLATION_CPI_INFO = ROOT_DIR / 'data' / 'za_inflation_cpi.json'
ZA_INFLATION_PPI_DATA = ROOT_DIR / 'data' / 'za_inflation_ppi.csv'
ZA_INFLATION_PPI_INFO = ROOT_DIR / 'data' / 'za_inflation_ppi.json'
