import numpy as np

X = np.array([
    [25, 50000],
    [17, 30000],
    [35, 80000],
    [42, 90000],
    [19, 25000],
    [31, 70000]
])

# Part 1
age_mask = X[:, 0] >= 25
print("Age greater than or equal to 25:")
print(X[age_mask])

# Part 2
salary_mask = X[:, 1] > 60000
print("\nSalary greater than 60000:")
print(X[salary_mask])

# Part 3
print("\nAge >= 25 and salary > 60000:")
print(X[age_mask & salary_mask])

# Part 4
X[X[:, 1] < 30000, 1] = 30000
print("\nAfter replacing low salaries:")
print(X)

# Part 5
print("\nAverage salary:", np.mean(X[:, 1]))

# Part 6
print("Average salary for age >= 25:", np.mean(X[age_mask, 1]))
