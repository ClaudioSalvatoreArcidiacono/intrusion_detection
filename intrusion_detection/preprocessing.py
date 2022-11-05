def preprocess_data(df):
    df["attack_type"] = df.attack_type.str.replace(".", "", regex=False)
    return df
