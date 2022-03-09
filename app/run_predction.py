"""Entry point to run the prediction
project     : DS Meetup - Titanic Sample Project
maintainer  : Wedeueis Braz
email       : wedeueis.braz@artefact.com
"""

from src.models.prediction import run_predction

if __name__ == "__main__":
    df = run_predction()
    df.to_csv("../data/outputs/prediction.csv")
