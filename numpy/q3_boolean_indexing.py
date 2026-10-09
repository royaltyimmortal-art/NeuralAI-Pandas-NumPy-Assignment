import numpy as np

X = np.array([
    [25, 50000],
    [17, 30000],
    [35, 80000],
    [42, 90000],
    [19, 25000],
    [31, 70000]
])

age_filter = X[:, 0] >= 25
salary_filter = X[:, 1] > 60000

print("People whose age is 25 or more:")
print(X[age_filter])

print("\nPeople whose salary is greater than 60000:")
print(X[salary_filter])

print("\nPeople aged 25 or more with salary greater than 60000:")
print(X[age_filter & salary_filter])

X[X[:, 1] < 30000, 1] = 30000

print("\nAfter replacing salaries below 30000:")
print(X)

print("\nAverage salary:", X[:, 1].mean())
print("Average salary for people aged 25 or more:",
      X[age_filter, 1].mean())
