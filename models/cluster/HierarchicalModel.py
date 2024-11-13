from scipy.cluster.hierarchy import linkage, fcluster
from scipy.spatial.distance import pdist, cdist
import numpy as np


class HierarchicalModel:
    def __init__(self, n_clusters=20, method='average', metric='euclidean'):
        self.n_clusters = n_clusters
        self.method = method
        self.metric = metric
        self.fit_data = None  # This will store the data after fitting
        self.fit_clusters = None  # This will store the clusters after fitting
    
    def fit_predict(self, data):
        self.fit_data = data  # Store the fitting data
        # Compute the pairwise distance matrix
        distance_matrix = pdist(self.fit_data, metric=self.metric)
        # Perform hierarchical clustering
        distances = linkage(distance_matrix, method=self.method)
        # Assign clusters
        clusters = fcluster(distances, self.n_clusters, criterion='maxclust')
        self.fit_clusters = clusters  # Store the clusters
        return clusters, distances

    def predict(self, new_data):
        if self.fit_data is None:
            raise ValueError("Model has not been fitted yet. Please call fit_predict first.")
        unique_clusters = np.unique(self.fit_clusters)
        centroids = np.array([np.mean(self.fit_data[self.fit_clusters == i], axis=0) for i in unique_clusters])
        distances_to_centroids = cdist(new_data, centroids, metric=self.metric)
        predicted_clusters = unique_clusters[np.argmin(distances_to_centroids, axis=1)]
        return predicted_clusters