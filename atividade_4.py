import numpy as np

A = np.array([[10, 7, 8, 7], [7, 5, 6, 5], [8, 6, 10, 9], [7, 5, 9, 10]])
B = np.array([32, 23, 33, 31])
print(np.dot(np.linalg.inv(A), B))   