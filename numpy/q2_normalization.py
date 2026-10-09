import numpy as np

X = np.array([
    [10, 100, 1000],
    [20, 200, 2000],
    [30, 300, 3000],
    [40, 400, 4000],
    [50, 500, 5000]
])

mean = X.mean(axis=0)
std = X.std(axis=0)

print("Mean of each column:")
print(mean)

print("\nStandard deviation of each column:")
print(std)

X_scaled = (X - mean) / std

print("\nScaled matrix:")
print(X_scaled)

print("\nMean of each scaled column:")
print(X_scaled.mean(axis=0))

print("\nStandard deviation of each scaled column:")
print(X_scaled.std(axis=0))
