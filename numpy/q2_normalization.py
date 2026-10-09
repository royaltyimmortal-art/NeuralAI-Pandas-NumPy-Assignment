import numpy as np

X = np.array([
    [10, 100, 1000],
    [20, 200, 2000],
    [30, 300, 3000],
    [40, 400, 4000],
    [50, 500, 5000]
])

# Part 1
mean = np.mean(X, axis=0)
print("Column means:", mean)

# Part 2
std = np.std(X, axis=0)
print("Column standard deviations:", std)

# Part 3
X_scaled = (X - mean) / std

# Part 4
print("\nScaled matrix:")
print(X_scaled)

# Part 5
print("\nScaled column means:", np.mean(X_scaled, axis=0))
print("Scaled column standard deviations:", np.std(X_scaled, axis=0))
