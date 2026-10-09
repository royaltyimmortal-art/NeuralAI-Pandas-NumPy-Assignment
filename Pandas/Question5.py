import pandas as pd
import numpy as np

data = {"Age": [20, 25, 30, 35, 40, 45, 50, 55], "Salary": [25000, 30000, 40000, 50000, 60000, 70000, 80000, 90000], "Experience": [1, 2, 5, 7, 10, 12, 15, 20], "City": ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai", "Delhi", "Pune", "Delhi"], "Purchased": [0, 0, 0, 1, 1, 1, 1, 1]}
df = pd.DataFrame(data)

#part 1
X = df.drop("Purchased", axis=1)
y = df["Purchased"]

#part 2
X = pd.get_dummies(X, columns=["City"], dtype=int)

#part 3
X = X.to_numpy(dtype=float)
y = y.to_numpy()

#part 4
print(X.shape)
print(y.shape)

#part 5
np.random.seed(0)
order = np.random.permutation(len(X))
X = X[order]
y = y[order]

#part 6
split = int(0.8 * len(X))
X_train = X[:split]
X_test = X[split:]
y_train = y[:split]
y_test = y[split:]

#part 7
mean = np.mean(X_train, axis=0)
std = np.std(X_train, axis=0)

#part 8 and part 9
X_train = (X_train - mean) / std
X_test = (X_test - mean) / std

#part 10
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

#part 11
print(X_train)
print(X_test)
print(y_train)
print(y_test)
