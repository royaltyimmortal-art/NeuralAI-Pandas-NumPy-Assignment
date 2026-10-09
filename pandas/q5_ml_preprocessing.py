import pandas as pd
import numpy as np

data = {
    "Age": [20, 25, 30, 35, 40, 45, 50, 55],
    "Salary": [25000, 30000, 40000, 50000, 60000, 70000, 80000, 90000],
    "Experience": [1, 2, 5, 7, 10, 12, 15, 20],
    "City": ["Delhi", "Mumbai", "Delhi", "Pune",
             "Mumbai", "Delhi", "Pune", "Delhi"],
    "Purchased": [0, 0, 0, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

# Parts 1 and 2
X = df.drop("Purchased", axis=1)
y = df["Purchased"]
X = pd.get_dummies(X, columns=["City"], dtype=int)

# Parts 3 and 4
X = X.to_numpy(dtype=float)
y = y.to_numpy()
print("X shape:", X.shape)
print("y shape:", y.shape)

# Part 5
np.random.seed(0)
order = np.random.permutation(len(X))
X = X[order]
y = y[order]

# Part 6
split = int(0.8 * len(X))
X_train = X[:split]
X_test = X[split:]
y_train = y[:split]
y_test = y[split:]

# Parts 7, 8 and 9
mean = np.mean(X_train, axis=0)
std = np.std(X_train, axis=0)
X_train = (X_train - mean) / std
X_test = (X_test - mean) / std

# Part 10
print("\nX_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)

# Part 11
print("\nX_train:")
print(X_train)
print("\nX_test:")
print(X_test)
print("\ny_train:")
print(y_train)
print("\ny_test:")
print(y_test)
