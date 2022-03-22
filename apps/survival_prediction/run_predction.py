"""Entry point to run the prediction
project     : DS Meetup - Titanic Sample Project
maintainer  : Wedeueis Braz
email       : wedeueis.braz@artefact.com
"""
import os
import sys

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
)
sys.path.append(PROJECT_ROOT)

import pandas as pd
import numpy as np

from src.data_cleaning import clean
from src.make_features import create_new_features
from src.prediction import predict


def run_prediction():
    df = pd.read_csv(os.path.join(PROJECT_ROOT, "data/raw/test.csv"))
    df.set_index("PassengerId")
    df["Survived"] = np.nan
    df = clean(df)
    df = create_new_features(df)
    df["Survived"] = predict(df)
    df[["Survived"]].to_csv(os.path.join(PROJECT_ROOT, "data/outputs/prediction.csv"))


if __name__ == "__main__":
    run_prediction()
