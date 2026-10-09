import numpy as np

X = np.array([
    [1, 2],
    [2, 3],
    [3, 4],
    [4, 5],
    [5, 6]
])

y = np.array([3, 5, 7, 9, 11])

# Part 1
X = np.column_stack((np.ones(len(X)), X))

# Part 2
XTX = X.T @ X

# Part 3
XTy = X.T @ y

# Part 4
w = np.linalg.pinv(XTX) @ XTy

# Part 5
y_pred = X @ w

# Part 6
mse = np.sum((y - y_pred) ** 2) / len(y)

# Part 7
print("Weights:", w)
print("Predictions:", y_pred)
print("MSE:", mse)
