import numpy as np
from sklearn.base import BaseEstimator
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples


class DDOSDetector(BaseEstimator):
    def __init__(
        self, n_clusters=3, sample_size_silhouette=10000, n_normal_clusters=1
    ) -> None:
        self.n_clusters = n_clusters
        self.sample_size_silhouette = sample_size_silhouette
        self.n_normal_clusters = n_normal_clusters

    def fit(self, X, y=None):
        self.cluster_ = KMeans(n_clusters=self.n_clusters).fit(X)
        clustering_preds = self.cluster_.predict(X)
        sampled_index = np.random.choice(
            np.arange(0, X.shape[0], dtype=int),
            self.sample_size_silhouette,
            replace=False,
        )
        silhouette_scores = silhouette_samples(
            X.iloc[sampled_index], clustering_preds[sampled_index]
        )
        means_lst = []
        for label in range(self.n_clusters):
            means_lst.append(
                silhouette_scores[clustering_preds[sampled_index] == label].mean()
            )

        self.normal_classes_ = np.argsort(means_lst)[: self.n_normal_clusters]
        return self

    def predict(self, X):
        clustering_preds = self.cluster_.predict(X)
        return np.logical_not(np.isin(clustering_preds, self.normal_classes_)).astype(
            int
        )
