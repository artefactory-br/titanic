"""Entry point to run the model fitting
project     : DS Meetup - Titanic Sample Project
maintainer  : Wedeueis Braz
email       : wedeueis.braz@artefact.com
"""

import pandas as pd

from src.preprocess.data_cleaning import clean
from src.features.make_features import create_new_features
from src.models.train import fit_model


def run_training():
    df = pd.read_csv("../data/processed/model_input.csv")
    df = clean(df)
    df = create_new_features(df)
    fit_model(df)


if __name__ == "__main__":
    df = run_training()
