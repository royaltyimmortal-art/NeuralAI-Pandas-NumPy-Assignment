import pandas as pd

data = {"Age": [20, 21, None, 24, None, 30], "Salary": [30000, None, 40000, 50000, None, 60000], "Experience": [1, 2, 3, None, 5, 6], "Department": ["CS", "IT", "CS", None, "IT", "CS"]}
df = pd.DataFrame(data)

#part 1
print(df)

#part 2
print(df.isnull().sum())

#part 3
df["Age"] = df["Age"].fillna(df["Age"].median())

#part 4
df["Salary"] = df["Salary"].fillna(df["Salary"].median())

#part 5
df["Experience"] = df["Experience"].fillna(df["Experience"].median())

#part 6
df["Department"] = df["Department"].fillna(df["Department"].mode()[0])

#part 7
print(df.isnull().sum())

#part 8
print(df)
