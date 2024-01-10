from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import numpy as np

# Generate sample data
X, _ = make_blobs(n_samples=100, centers=3, cluster_std=1.0)

# Initialize KMeans
kmeans = KMeans(n_clusters=3)

# Fit KMeans to data
kmeans.fit(X)

# Get cluster centroids and labels
centroids = kmeans.cluster_centers_
labels = kmeans.labels_

# Print cluster centroids and labels
print("Centroids:")
print(centroids)
print("\nLabels:")
print(labels)