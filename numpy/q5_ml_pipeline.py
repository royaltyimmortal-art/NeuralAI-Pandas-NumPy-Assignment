import numpy as np

X = np.array([
    [1, 10],
    [2, 20],
    [3, 30],
    [4, 40],
    [5, 50],
    [6, 60],
    [7, 70],
    [8, 80],
    [9, 90],
    [10, 100]
])

y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

np.random.seed(42)
indices = np.random.permutation(len(X))

X = X[indices]
y = y[indices]

split = int(0.8 * len(X))

X_train = X[:split]
X_test = X[split:]
y_train = y[:split]
y_test = y[split:]

mean = np.mean(X_train, axis=0)
std = np.std(X_train, axis=0)

X_train_scaled = (X_train - mean) / std
X_test_scaled = (X_test - mean) / std

print("Shapes:")
print("X_train:", X_train.shape)
print("X_test:", X_test.shape)
print("y_train:", y_train.shape)
print("y_test:", y_test.shape)

print("\nFirst 3 training samples before scaling:")
print(X_train[:3])

print("\nFirst 3 training samples after scaling:")
print(X_train_scaled[:3])

print("\nMean of the scaled training features:")
print(np.mean(X_train_scaled, axis=0))

print("\nStandard deviation of the scaled training features:")
print(np.std(X_train_scaled, axis=0))
