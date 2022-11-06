def define_target(df):
    df["target_anomaly"] = (
        ~df["attack_type"].isin(["normal", "smurf", "neptune"])
    ).astype(int)
    df["target_ddos"] = (
        df["attack_type"].isin(["smurf", "neptune"])
    ).astype(int)
    return df
