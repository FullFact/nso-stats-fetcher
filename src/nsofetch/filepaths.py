from pathlib import Path
import os

ROOT_DIR = Path(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..")))
DATA_DIR = ROOT_DIR / "data"

NSO_STATS_METADATA = ROOT_DIR / "data" / "nso_stats_metadata.json"
