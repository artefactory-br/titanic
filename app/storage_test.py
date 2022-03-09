import sys
from os import path
import json

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from dotenv import load_dotenv

load_dotenv()

from src.utils.datasource import read_dataframe_from_bucket_file

FILENAME = "DS-Meetup/titanic/data/raw/train.csv"
BUCKET_NAME = "wedeueis-braz"

print(read_dataframe_from_bucket_file(BUCKET_NAME, FILENAME, sep=","))


with open("config/local/config.json") as file:
    config = json.load(file)
    user = config["database_username"]
    password = config["database_password"]
    print(user)
