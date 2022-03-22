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

from src.config import project_root, config

modelling_config = config["params"]["modelling"]
model_save_path = os.path.join(
    project_root,
    modelling_config["save_path"].format(modelling_config["name"]),
)


def fit_model(df, save_path=None):
    df.set_index("PassengerId", inplace=True)
    model = create_model(df)
    save_pipeline(model=model, path=save_path)


def create_model(df):
    model_setup = setup(
        data=df,
        target=modelling_config["target"],
        numeric_features=modelling_config["numeric_features"],
        train_size=modelling_config["train_size"],
        normalize=modelling_config["normalize"] == 1,
        ignore_low_variance=modelling_config["ignore_low_variance"] == 1,
        combine_rare_levels=modelling_config["combine_rare_levels"] == 1,
        remove_multicollinearity=modelling_config["remove_multicollinearity"] == 1,
        feature_selection=modelling_config["feature_selection"] == 1,
        silent=modelling_config["silent"] == 1,
        fold_strategy="stratifiedkfold",
        fold=modelling_config["cv_folds"],
    )
    model = compare_models()
    model_tunned = tune_model(
        model,
        optimize=modelling_config["optimize_metric"],
        n_iter=modelling_config["optimize_iter"],
    )
    return finalize_model(model_tunned)


def save_pipeline(model, path=None):
    if path is not None:
        save_model(model, path)
    else:
        save_model(model, model_save_path)
