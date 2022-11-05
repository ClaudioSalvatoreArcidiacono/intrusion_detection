from sklearn.base import BaseEstimator, TransformerMixin


class KeepInputFeaturesWrapper(BaseEstimator, TransformerMixin):
    def __init__(self, wrapped_transformer, rename_suffix=None):
        self.wrapped_transformer = wrapped_transformer
        self.rename_suffix = rename_suffix

    def fit(self, *args, **kwargs):
        self.wrapped_transformer.fit(*args, **kwargs)
        return self

    def transform(self, X, *args, **kwargs):
        to_keep = X[self.variables_].copy()
        X = self.wrapped_transformer.transform(X, *args, **kwargs)
        X = X.rename(
            columns={var: f"{var}{self.rename_suffix}" for var in self.variables_}
        )
        X[self.variables_] = to_keep
        return X

    def __getattr__(self, attr):
        """Forward calls to missing attributes to the wrapped clf instance.

        Args:
            attr (str): attribute name to access.

        Returns:
            Any: Attribute value.
        """
        return getattr(self.wrapped_transformer, attr)
