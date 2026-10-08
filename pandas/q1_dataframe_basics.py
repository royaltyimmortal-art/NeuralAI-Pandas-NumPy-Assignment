import pandas as pd

data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Age": [20, 25, 22, 30, 28],
    "Marks": [85, 72, 90, 65, 88],
    "City": ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai"]
}

df = pd.DataFrame(data)

print("First 3 rows:")
print(df.head(3))

print("\nLast 2 rows:")
print(df.tail(2))

print("\nShape:", df.shape)

print("\nColumn names:")
print(df.columns)

print("\nData types:")
print(df.dtypes)

print("\nName and Marks columns:")
print(df[["Name", "Marks"]])

print("\nStudents whose marks are greater than 80:")
print(df[df["Marks"] > 80])

print("\nStudents sorted by marks from highest to lowest:")
print(df.sort_values(by="Marks", ascending=False))
