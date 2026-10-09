import numpy as np

X = np.array([[10, 100, 1000], [20, 200, 2000], [30, 300, 3000], [40, 400, 4000], [50, 500, 5000]])

#part 1
mean = np.mean(X, axis=0)
print(mean)

#part 2
std = np.std(X, axis=0)
print(std)

#part 3 and part 6
X_scaled = (X - mean) / std

#part 4
print(X_scaled)

#part 5
print(np.mean(X_scaled, axis=0))
print(np.std(X_scaled, axis=0))
