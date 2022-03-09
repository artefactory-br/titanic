"""Functions to generate the new features for modelling
project     : DS Meetup - Titanic Sample Project
maintainer  : Wedeueis Braz
email       : wedeueis.braz@artefact.com
"""

import json

import pandas as pd


def create_new_features(df):
    with open("../../config/shared/config.json") as file:
        config = json.loads(file)
        df = feature_alone(df)
        df = feature_dummies(df, config["params"]["feature_eng"]["dummify_feature"])

        return df


def feature_alone(df):
    raise NotImplementedError("Error: function not implemented")


def feature_dummies(df, cols):
    raise NotImplementedError("Error: function not implemented")
