"""Entry point to run the model fitting
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

from src.data_cleaning import clean
from src.make_features import create_new_features
from src.train import fit_model


def run_training():
    df = pd.read_csv(os.path.join(PROJECT_ROOT, "data/raw/train.csv"))
    df = clean(df)
    df = create_new_features(df)
    fit_model(df)


if __name__ == "__main__":
    df = run_training()
