import subprocess
import os
from pathlib import Path
import zipfile


project_dir = Path(__file__).resolve().parent.parent
data_dir = project_dir / "raw_data"

url = "https://archive.ics.uci.edu/static/public/179/secom.zip"

os.makedirs(data_dir, exist_ok=True)
subprocess.run(["wget", url, "-P", data_dir])

zip_file_path = data_dir / "secom.zip"

with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(data_dir)