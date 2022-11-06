import logging
import sys
import warnings

import joblib
import pandas as pd
from fire import Fire

from intrusion_detection.load_input_data import load_df

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


def main(
    data_path="data/kddcup.data_10_percent",
    header_file="data/kddcup.names",
    model_file="frozen_models/model.joblib",
    predictions_file="data/model_predictions.csv",
):
    logging.info(f"Loading Data from {data_path} and headers from {header_file}")
    df = load_df(file_path=data_path, header_file=header_file)
    logging.info(f"Data Loaded, Number of rows = {df.shape[0]}")
    logging.info(f"Loading pre-trained model from {model_file}")
    final_model_pipeline = joblib.load(model_file)
    logging.info("Start Predicting")
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=UserWarning)
        predictions = final_model_pipeline.predict(df)
    predictions_df = pd.DataFrame({"is_cyber_attack": predictions})
    logging.info("Prediction Finished, saving predictions to file")
    predictions_df.to_csv(predictions_file)
    logging.info(f"Model Saved at {predictions_file}")


if __name__ == "__main__":
    Fire(main)
