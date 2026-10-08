import numpy as np

X = np.array([
    [1, 2],
    [2, 3],
    [3, 4],
    [4, 5],
    [5, 6]
])

y = np.array([3, 5, 7, 9, 11])

# Add a column of ones as the bias column.
X = np.column_stack((np.ones(X.shape[0]), X))

print("X with bias column:")
print(X)

X_transpose_X = X.T @ X
X_transpose_y = X.T @ y

print("\nX.T @ X:")
print(X_transpose_X)

print("\nX.T @ y:")
print(X_transpose_y)

# The given columns are linearly dependent, so X.T @ X is singular.
# The pseudoinverse is the correct NumPy alternative in this case.
weights = np.linalg.pinv(X_transpose_X) @ X_transpose_y
predictions = X @ weights
mse = np.mean((y - predictions) ** 2)

print("\nWeights:")
print(weights)

print("\nPredictions:")
print(predictions)

print("\nMSE:")
print(mse)
