import pandas as pd
import numpy as np

data = {
    "Age": [20, 25, 30, 35, 40, 45, 50, 55],
    "Salary": [25000, 30000, 40000, 50000, 60000, 70000, 80000, 90000],
    "Experience": [1, 2, 5, 7, 10, 12, 15, 20],
    "City": [
        "Delhi", "Mumbai", "Delhi", "Pune",
        "Mumbai", "Delhi", "Pune", "Delhi"
    ],
    "Purchased": [0, 0, 0, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

# Separate the input features and target.
X = df.drop("Purchased", axis=1)
y = df["Purchased"]

# Convert the City values into numeric one-hot columns.
X = pd.get_dummies(X, columns=["City"], dtype=int)

X = X.to_numpy(dtype=float)
y = y.to_numpy()

print("Original NumPy array shapes:")
print("X:", X.shape)
print("y:", y.shape)

np.random.seed(42)
shuffled_indices = np.random.permutation(len(X))

X = X[shuffled_indices]
y = y[shuffled_indices]

split_index = int(0.8 * len(X))

X_train = X[:split_index]
X_test = X[split_index:]
y_train = y[:split_index]
y_test = y[split_index:]

train_mean = np.mean(X_train, axis=0)
train_std = np.std(X_train, axis=0)

# A standard deviation of 0 cannot be used as a divisor.
# Replacing it with 1 keeps a constant feature unchanged after centering.
train_std = np.where(train_std == 0, 1, train_std)

X_train = (X_train - train_mean) / train_std
X_test = (X_test - train_mean) / train_std

print("\nTraining and testing shapes:")
print("X_train.shape:", X_train.shape)
print("X_test.shape:", X_test.shape)
print("y_train.shape:", y_train.shape)
print("y_test.shape:", y_test.shape)

print("\nFinal X_train array:")
print(X_train)

print("\nFinal X_test array:")
print(X_test)

print("\nFinal y_train array:")
print(y_train)

print("\nFinal y_test array:")
print(y_test)
