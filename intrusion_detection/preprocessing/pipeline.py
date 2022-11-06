from feature_engine.encoding import (
    CountFrequencyEncoder,
    OneHotEncoder,
    RareLabelEncoder,
)
from feature_engine.outliers import Winsorizer
from feature_engine.selection import DropFeatures
from feature_engine.wrappers import SklearnTransformerWrapper
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler

from .keep_input_features_wrapper import KeepInputFeaturesWrapper


def get_preprocessing_pipeline():
    return Pipeline(
        [
            ("drop_target", DropFeatures(["attack_type"])),
            (
                "outlier_removal",
                Winsorizer(
                    capping_method="quantiles",
                    variables=["src_bytes", "dst_bytes"],
                    tail="right",
                    fold=0.01,
                    add_indicators=True,
                ),
            ),
            (
                "frequency_encoder",
                KeepInputFeaturesWrapper(
                    CountFrequencyEncoder(encoding_method="frequency", unseen="encode"),
                    rename_suffix="_freq",
                ),
            ),
            ("replace_rare_categories", RareLabelEncoder(n_categories=2, tol=0.01)),
            ("one_hot_encoder", OneHotEncoder()),
            ("min_max_scaler", SklearnTransformerWrapper(MinMaxScaler())),
        ]
    )
