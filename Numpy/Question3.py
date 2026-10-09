import numpy as np

X = np.array([[25, 50000], [17, 30000], [35, 80000], [42, 90000], [19, 25000], [31, 70000]])

#part 1
age_mask = X[:, 0] >= 25
print(X[age_mask])

#part 2
salary_mask = X[:, 1] > 60000
print(X[salary_mask])

#part 3
print(X[age_mask & salary_mask])

#part 4
X[X[:, 1] < 30000, 1] = 30000
print(X)

#part 5
print(np.mean(X[:, 1]))

#part 6
print(np.mean(X[age_mask, 1]))
