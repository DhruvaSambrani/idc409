# Clustering

Used when classes are not known to find subtypes, or to classify when few data points are classified.

# K Means

- Make $k$ random clusters of same size
- Calc centroid of each cluster
- Find dist from each centroid and each vector.
- For each vector, find nearest centroid and put into that cluster
- Repeat until changes are minimal.
- Sum of intraclusteral distances can also be minimized, or stabilized.

# Hierarchical clustering

- Calc all pairwise distances
- Find nearest pairs and cluster
- Calc all pairwise distances between clusters
  - average linkage - find average of all distances
  - nearest/single linkage
  - complete linkage
  - centroid linkage
- Group nearest clusters
- repeat until cluster size is n
- Cut the tree to find cluster points
  - cut level can be found by minimizing d(#cluster)/d(level)

# DBSCAN

- Draw radius r circle around every point
  - If n>2 other points lie in circle, point is core
  - If n==1 other points lie in circle, point is border
  - If n==0 , point is outlier
- For all core points,
  - Connect all core points in radius r
  - Connect border to closest core.
- Outliers ignored
- Robust against noise

# Comparision

| DBSCAN                   | K Means                      |
| ------------------------ | ---------------------------- |
| Noise resistant          | No noise resistance          |
| Captures arbitrary shape | Captures Spherical shapes    |
| Slower and counts noise  | Faster for large/sparse      |
| Actual clusters          | exactly k clusters are given |


