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

split = int(len(X) * 0.8)

X_train = X[:split]
X_test = X[split:]
y_train = y[:split]
y_test = y[split:]

train_mean = X_train.mean(axis=0)
train_std = X_train.std(axis=0)

X_train_scaled = (X_train - train_mean) / train_std
X_test_scaled = (X_test - train_mean) / train_std

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
print(X_train_scaled.mean(axis=0))

print("\nStandard deviation of the scaled training features:")
print(X_train_scaled.std(axis=0))
