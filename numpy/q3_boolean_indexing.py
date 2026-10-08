import numpy as np

X = np.array([
    [25, 50000],
    [17, 30000],
    [35, 80000],
    [42, 90000],
    [19, 25000],
    [31, 70000]
])

print("People whose age is 25 or more:")
print(X[X[:, 0] >= 25])

print("\nPeople whose salary is greater than 60000:")
print(X[X[:, 1] > 60000])

print("\nPeople aged 25 or more with salary greater than 60000:")
print(X[(X[:, 0] >= 25) & (X[:, 1] > 60000)])

X[X[:, 1] < 30000, 1] = 30000

print("\nAfter replacing salaries below 30000:")
print(X)

print("\nAverage salary:", np.mean(X[:, 1]))
print("Average salary for people aged 25 or more:",
      np.mean(X[X[:, 0] >= 25, 1]))
