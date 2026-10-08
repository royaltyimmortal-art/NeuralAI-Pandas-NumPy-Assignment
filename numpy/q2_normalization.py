import numpy as np

X = np.array([
    [10, 100, 1000],
    [20, 200, 2000],
    [30, 300, 3000],
    [40, 400, 4000],
    [50, 500, 5000]
])

# axis=0 calculates each column separately.
column_mean = np.mean(X, axis=0)
column_std = np.std(X, axis=0)

print("Mean of each column:")
print(column_mean)

print("\nStandard deviation of each column:")
print(column_std)

# NumPy broadcasting applies the column values to every row.
X_scaled = (X - column_mean) / column_std

print("\nScaled matrix:")
print(X_scaled)

print("\nMean of each scaled column:")
print(np.mean(X_scaled, axis=0))

print("\nStandard deviation of each scaled column:")
print(np.std(X_scaled, axis=0))
