"""Functions to generate the prediction with a trianed model
project     : DS Meetup - Titanic Sample Project
maintainer  : Wedeueis Braz
email       : wedeueis.braz@artefact.com
"""

import os

from pycaret.classification import load_model

from src.config import project_root, config

modelling_config = config["params"]["modelling"]
model_save_path = os.path.join(
    project_root,
    modelling_config["save_path"].format(modelling_config["name"]),
)


def load_pipeline(path=None):
    if path is not None:
        model = load_model(path)
    else:
        model = load_model(model_save_path)
    return model


def predict(df):
    model = load_pipeline()
    return model.predict(df)
