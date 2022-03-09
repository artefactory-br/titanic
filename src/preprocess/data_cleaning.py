"""Functions to clean the dataset
project     : DS Meetup - Titanic Sample Project
maintainer  : Wedeueis Braz
email       : wedeueis.braz@artefact.com
"""

import json

import pandas as pd


def clean(df):
    with open("../../config/shared/config.json") as file:
        config = json.loads(file)
        df = fillna_cols(df, config["params"]["cleaning"]["filna_map"])
        df = filter_cols(df, config["params"]["cleaning"]["filter_cols"])

        return df


def fillna_cols(df, map):
    raise NotImplementedError("Error: function not implemented")


def filter_cols(df, cols=None):
    raise NotImplementedError("Error: function not implemented")
