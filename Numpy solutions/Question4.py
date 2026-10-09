import numpy as np

X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
y = np.array([3, 5, 7, 9, 11])

#part 1
X = np.column_stack((np.ones(len(X)), X))

#part 2
XTX = X.T @ X

#part 3
XTy = X.T @ y

#part 4
w = np.linalg.pinv(XTX) @ XTy

#part 5
y_pred = X @ w

#part 6
mse = np.sum((y - y_pred) ** 2) / len(y)

#part 7
print(w)
print(y_pred)
print(mse)
