"""Functions to fit a new model
project     : DS Meetup - Titanic Sample Project
maintainer  : Wedeueis Braz
email       : wedeueis.braz@artefact.com
"""

import os

from pycaret.classification import (
    setup,
    compare_models,
    tune_model,
    finalize_model,
    save_model,
)

from src.config import project_root, shared_config

model_save_path = os.path.join(
    project_root,
    shared_config["params"]["modelling"]["save_path"].format("survival_classifier"),
)


def fit_model(df, save_path=None):
    df.set_index("PassengerId", inplace=True)
    model = create_model(df)
    save_pipeline(model=model, path=save_path)


def create_model(df):
    model_setup = setup(
        data=df,
        target="Survived",
        numeric_features=["Age", "Fare", "SibSp", "Parch"],
        train_size=0.75,
        normalize=True,
        ignore_low_variance=True,
        combine_rare_levels=True,
        remove_multicollinearity=True,
        feature_selection=True,
        silent=True,
        fold_strategy="stratifiedkfold",
        fold=10,
    )
    model = compare_models()
    model_tunned = tune_model(model, optimize="F1", n_iter=15)
    return finalize_model(model_tunned)


def save_pipeline(model, path=None):
    if path is not None:
        save_model(model, path)
    else:
        save_model(model, model_save_path)
