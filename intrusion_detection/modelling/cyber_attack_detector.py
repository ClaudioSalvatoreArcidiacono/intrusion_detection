import numpy as np
from sklearn.base import BaseEstimator


class CyberAttackDetector(BaseEstimator):
    def __init__(
        self, preprocessing_pipeline, ddos_detector_pipeline, anomaly_detection_pipeline
    ) -> None:
        self.preprocessing_pipeline = preprocessing_pipeline
        self.ddos_detector_pipeline = ddos_detector_pipeline
        self.anomaly_detection_pipeline = anomaly_detection_pipeline

    def fit(self, X, y=None):
        X_preprocessed = self.preprocessing_pipeline.fit_transform(X)
        ddos_preds = self.ddos_detector_pipeline.fit(X_preprocessed).predict(
            X_preprocessed
        )
        self.anomaly_detection_pipeline.fit(X_preprocessed.loc[ddos_preds == 0])
        return self

    def predict(self, X):
        return (self.predict_proba(X)[:, 1] >= 0.5).astype(int)

    def predict_proba(self, X):
        X_preprocessed = self.preprocessing_pipeline.transform(X)
        preds = self.ddos_detector_pipeline.predict(X_preprocessed)
        no_ddos_connections = X_preprocessed.loc[preds == 0]
        if no_ddos_connections.shape[0] > 0:
            anomaly_preds = self.anomaly_detection_pipeline.predict_proba(
                no_ddos_connections
            )[:, 1]
            preds[preds == 0] = anomaly_preds
        return np.c_[1 - preds, preds]
