"""Functions to generate the prediction with a trianed model
project     : DS Meetup - Titanic Sample Project
maintainer  : Wedeueis Braz
email       : wedeueis.braz@artefact.com
"""

import os

from pycaret.classification import load_model

from src.config import project_root, shared_config

model_save_path = os.path.join(
    project_root,
    shared_config["params"]["modelling"]["save_path"].format("survival_classifier"),
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
