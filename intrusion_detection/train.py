import logging
import sys

import joblib
from fire import Fire

from intrusion_detection.load_input_data import load_df
from intrusion_detection.modelling.final_model_pipeline import get_final_model_pipeline

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


def main(
    data_path="data/kddcup.data_10_percent",
    header_file="data/kddcup.names",
    output_model_file="frozen_models/model.joblib",
):
    logging.info(f"Loading Data from {data_path} and headers from {header_file}")
    df = load_df(file_path=data_path, header_file=header_file)
    logging.info(f"Data Loaded, Number of rows = {df.shape[0]}")
    final_model_pipeline = get_final_model_pipeline(df)
    logging.info("Start Training Model")
    final_model_pipeline.fit(df)
    logging.info("Training Finished, Saving the model")
    joblib.dump(final_model_pipeline, output_model_file)
    logging.info(f"Model Saved at {output_model_file}")


if __name__ == "__main__":
    Fire(main)
