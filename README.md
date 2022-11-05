# Intrusion Detection

In this repository an unsupervised intrusion detection model is developed and wrapped around an API server.

In order to train and evaluate the model, data from the 1999 edition of the KDD challenge have been used.

## Python Virtualenvironment management

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