from sklearn.base import TransformerMixin


class RareCategoryReplacer(TransformerMixin):
    """Replace rare categories with a default value."""

    def __init__(
        self, variables=None, min_frequency=0.01, cat_value_to_replace="is_rare"
    ):
        self.variables = variables
        self.min_frequency = min_frequency
        self.cat_value_to_replace = cat_value_to_replace

    def fit(self, X, y=None):
        if self.variables:
            self.variables = list(set(self.variables) & set(X.columns))
        else:
            self.variables = X.select_dtypes(object).columns

        self.frequent_categorical_values_ = {}

        min_number_of_instances = int(X.shape[0]) * self.min_frequency
        for col in self.variables:
            value_counts = X[col].value_counts()
            frequent_values = value_counts[
                value_counts >= min_number_of_instances
            ].index.to_list()
            self.frequent_categorical_values_[col] = frequent_values
        return self

    def transform(self, X, y=None):
        X = X.copy()
        for col, frequent_values in self.frequent_categorical_values_.items():
            X.loc[~X[col].isin(frequent_values), col] = self.cat_value_to_replace

        if y:
            return X, y
        else:
            return X
