"""Functions to generate the new features for modelling
project     : DS Meetup - Titanic Sample Project
maintainer  : Wedeueis Braz
email       : wedeueis.braz@artefact.com
"""

import pandas as pd

from src.config import config


def create_new_features(df):
    df = feature_alone(df)
    df = feature_dummies(df, config["params"]["feature_eng"]["dummify_feature"])
    return df[
        [
            "PassengerId",
            "Age",
            "SibSp",
            "Parch",
            "Fare",
            "Alone",
            "Pclass_1",
            "Pclass_2",
            "Sex_female",
            "Embarked_C",
            "Embarked_Q",
            "Survived",
        ]
    ]


def feature_alone(df):
    df["Alone"] = ((df["SibSp"] + df["Parch"]) > 0) * 1
    return df


def feature_dummies(df, cols):
    df = pd.get_dummies(df, columns=cols)
    return df
