import sys
import os

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
)
sys.path.append(PROJECT_ROOT)

from dotenv import load_dotenv

load_dotenv()

from src.datasource import read_dataframe_from_bucket_file

FILENAME = "<path-to-the-file>"
BUCKET_NAME = "<bucket-name>"

print(read_dataframe_from_bucket_file(BUCKET_NAME, FILENAME, sep=","))
