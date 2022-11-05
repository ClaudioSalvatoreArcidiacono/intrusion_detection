import pandas as pd


def load_df(
    file_path="data/kddcup.data_10_percent", header_file="data/kddcup.names"
):
    with open(header_file) as header_file:
        header_raw = header_file.readlines()
    column_names = [h.split(":")[0] for h in header_raw[1:]]
    column_names.append("attack_type")
    df = pd.read_csv(file_path, names=column_names)
    return df
