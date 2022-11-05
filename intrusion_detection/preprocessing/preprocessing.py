def remove_dot_from_attack_type_classes(df):
    df["attack_type"] = df.attack_type.str.replace(".", "", regex=False)
    return df
