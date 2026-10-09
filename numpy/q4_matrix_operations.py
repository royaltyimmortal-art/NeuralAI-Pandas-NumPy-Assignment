import numpy as np

X = np.array([
    [1, 2],
    [2, 3],
    [3, 4],
    [4, 5],
    [5, 6]
])

y = np.array([3, 5, 7, 9, 11])

X = np.column_stack((np.ones(X.shape[0]), X))

print("X with bias column:")
print(X)

XTX = X.T @ X
XTy = X.T @ y

print("\nX.T @ X:")
print(XTX)

print("\nX.T @ y:")
print(XTy)

w = np.linalg.pinv(XTX) @ XTy
y_pred = X @ w
mse = np.sum((y - y_pred) ** 2) / len(y)

print("\nWeights:")
print(w)

print("\nPredictions:")
print(y_pred)

print("\nMSE:")
print(mse)
