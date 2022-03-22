"""Functions to clean the dataset
project     : DS Meetup - Titanic Sample Project
maintainer  : Wedeueis Braz
email       : wedeueis.braz@artefact.com
"""

from src.config import shared_config


def clean(df, cols=None):
    if cols is None:
        df = filter_cols(df, shared_config["params"]["cleaning"]["filter_cols"])
    else:
        df = filter_cols(df, cols)

    df = fillna_cols(df)
    return df


def fillna_cols(df):
    return df.fillna({"Age": df["Age"].mean(), "Embarked": df["Embarked"].mode()[0]})


def filter_cols(df, cols=None):
    if cols is not None:
        return df[cols]
    return df
