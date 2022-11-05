class KeepInputFeaturesWrapper:
    def __init__(self, wrapped_transformer, rename_suffix=None):
        self.wrapped_transformer = wrapped_transformer
        self.rename_suffix = rename_suffix

    def transform(self, X, *args, **kwargs):
        variables = self.wrapped_transformer.variables_
        to_keep = X[variables]
        X = self.wrapped_transformer.transform(X, *args, **kwargs)
        if self.rename_suffix:
            X = X.rename(
                columns={var: f"{var}{self.rename_suffix}" for var in variables}
            )
        X[variables] = to_keep
        return X

    def __getattr__(self, attr):
        """Forward calls to missing attributes to the wrapped clf instance.

        Args:
            attr (str): attribute name to access.

        Returns:
            Any: Attribute value.
        """
        return getattr(self.wrapped_transformer, attr)
