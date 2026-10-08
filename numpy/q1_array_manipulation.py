import numpy as np

X = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90],
    [100, 110, 120]
])

print("Shape:", X.shape)
print("Dimensions:", X.ndim)
print("Data type:", X.dtype)

print("\nSecond column:")
print(X[:, 1])

print("\nFirst two rows:")
print(X[:2])

print("\nLast two columns:")
print(X[:, -2:])

X_modified = X.copy()
X_modified[X_modified > 80] = 0

print("\nAfter replacing values greater than 80 with 0:")
print(X_modified)

print("\nMinimum of each column:", np.min(X_modified, axis=0))
print("Maximum of each column:", np.max(X_modified, axis=0))
print("Mean of each column:", np.mean(X_modified, axis=0))
print("Standard deviation of each column:", np.std(X_modified, axis=0))
