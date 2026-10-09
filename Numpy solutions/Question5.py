import numpy as np

X = np.array([[1, 10], [2, 20], [3, 30], [4, 40], [5, 50], [6, 60], [7, 70], [8, 80], [9, 90], [10, 100]])
y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

#part 1
np.random.seed(42)
order = np.random.permutation(len(X))
X = X[order]
y = y[order]

#part 2 and part 3
split = int(0.8 * len(X))
X_train = X[:split]
X_test = X[split:]
y_train = y[:split]
y_test = y[split:]

#part 4 and part 5
mean = np.mean(X_train, axis=0)
std = np.std(X_train, axis=0)
X_train_scaled = (X_train - mean) / std
X_test_scaled = (X_test - mean) / std

#part 6
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

#part 7
print(X_train[:3])
print(X_train_scaled[:3])

#part 8
print(np.mean(X_train_scaled, axis=0))
print(np.std(X_train_scaled, axis=0))
