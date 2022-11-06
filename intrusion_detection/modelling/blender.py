import numpy as np
from sklearn.base import BaseEstimator


class Blender(BaseEstimator):
    def __init__(self, models, blender_fn=np.mean):
        self.models = models
        self.blender_fn = blender_fn

    def fit(self, X, y=None):
        for model in self.models:
            model.fit(X, y)
        return self

    def predict(self, X):
        preds = [model.predict(X) for model in self.models]
        return self.blender_fn(preds, axis=0)

    def predict_proba(self, X):
        preds = [model.predict_proba(X)[:, 1] for model in self.models]
        blended_preds = self.blender_fn(preds, axis=0)
        return np.c_[1 - blended_preds, blended_preds]
