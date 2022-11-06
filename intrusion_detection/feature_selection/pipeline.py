from feature_engine.selection import DropConstantFeatures, DropCorrelatedFeatures
from sklearn.pipeline import Pipeline


def get_feature_selection_pipeline(numerical_columns):
    return Pipeline(
        [
            ("drop_constant_features", DropConstantFeatures(tol=0.99)),
            (
                "drop_correlated_features",
                DropCorrelatedFeatures(
                    variables=numerical_columns, confirm_variables=True
                ),
            ),
        ]
    )
