<!-- omit in TOC -->
# Intrusion Detection

In this repository an unsupervised intrusion detection model has been developed.

In order to train and evaluate the model, data from the 1999 edition of the KDD challenge have been used.

<!-- omit in TOC -->
## Table of contents

- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
  - [Python Virtual environment management](#python-virtual-environment-management)
  - [Training a new model](#training-a-new-model)
  - [Using a pre-trained model to perform inference](#using-a-pre-trained-model-to-perform-inference)
- [Model development details](#model-development-details)

## Repository Structure

```bash
.
├── Makefile
├── data # Train data
├── docs # Train data
    └── notebooks # Notebooks stored here
├── frozen_models # Pre trained models
├── intrusion_detection # Source code
├── mkdocs.yml
├── pyproject.toml
├── requirements.txt
└── README.md
```

I agree with the fact that it is weird to store notebooks inside the `docs` folder, however this was the quickest way to add notebooks into my mkdocs documentation.

## Getting Started

### Python Virtual environment management

1. Create virtual environment

    ```bash
    make env-create
    ```

2. Activate virtual environment

    ```bash
    source ./venv/bin/activate
    ```

3. Install dependencies

    ```bash
    make env-install
    ```

4. (During development) Update dependencies. First edit the `pyproject.toml` file, then run:

    ```bash
    make env-update
    ```

For more info on this python environment workflow, please check [my blogpost](https://claudiosalvatorearcidiacono.github.io/blog/software-engineering/2022/05/28/python-dependency-management-workflow-using-standard-tools.html) :)

### Training a new model

After creating and activating the environment with the required dependencies installed, run from the project folder in a terminal shell:

```bash
python intrusion_detection/train.py \
    --data_path=DATA_PATH \
    --header_file=HEADER_FILE \
    --output_model_file=OUTPUT_MODEL_FILE
```

This script will load training data from the files `DATA_PATH` and `HEADER_FILE`, will train a model and it will save it at the destination `OUTPUT_MODEL_FILE`

### Using a pre-trained model to perform inference

After creating and activating the environment with the required dependencies installed, run from the project folder in a terminal shell:

```bash
python intrusion_detection/predict.py \
    --data_path=DATA_PATH \
    --header_file=HEADER_FILE \
    --model_file=MODEL_FILE \
    --predictions_file=PREDICTIONS_FILE
```

This script will load the data to score from the files `DATA_PATH` and `HEADER_FILE`, it will load the pre-trained model saved at the location `MODEL_FILE`, ultimately it will score data using the model file and store predictions at the location `PREDICTIONS_FILE` in CSV format.

## Model development details

More information on how the model was developed available [Here](https://claudiosalvatorearcidiacono.github.io/intrusion_detection/).
