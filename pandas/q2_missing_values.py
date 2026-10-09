import pandas as pd

data = {
    "Age": [20, 21, None, 24, None, 30],
    "Salary": [30000, None, 40000, 50000, None, 60000],
    "Experience": [1, 2, 3, None, 5, 6],
    "Department": ["CS", "IT", "CS", None, "IT", "CS"]
}

df = pd.DataFrame(data)

# Part 1
print("Original DataFrame:")
print(df)

# Part 2
print("\nMissing values:")
print(df.isnull().sum())

# Parts 3 to 6
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Salary"] = df["Salary"].fillna(df["Salary"].median())
df["Experience"] = df["Experience"].fillna(df["Experience"].median())
df["Department"] = df["Department"].fillna(df["Department"].mode()[0])

# Part 7
print("\nMissing values after filling:")
print(df.isnull().sum())

# Part 8
print("\nCleaned DataFrame:")
print(df)
