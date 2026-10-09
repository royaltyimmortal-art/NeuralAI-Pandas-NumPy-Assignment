import numpy as np

X = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90],
    [100, 110, 120]
])

# Part 1
print("Shape:", X.shape)
print("Dimensions:", X.ndim)
print("Data type:", X.dtype)

# Part 2
print("\nSecond column:")
print(X[:, 1])

# Part 3
print("\nFirst two rows:")
print(X[:2])

# Part 4
print("\nLast two columns:")
print(X[:, -2:])

# Part 5
X = np.where(X > 80, 0, X)
print("\nAfter replacing values greater than 80:")
print(X)

# Part 6
print("\nMinimum:", np.min(X, axis=0))
print("Maximum:", np.max(X, axis=0))
print("Mean:", np.mean(X, axis=0))
print("Standard deviation:", np.std(X, axis=0))
