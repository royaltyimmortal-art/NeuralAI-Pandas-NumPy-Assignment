import pandas as pd

data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Age": [20, 25, 22, 30, 28],
    "Marks": [85, 72, 90, 65, 88],
    "City": ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai"]
}

df = pd.DataFrame(data)

# Part 1
print("First 3 rows:")
print(df.head(3))

# Part 2
print("\nLast 2 rows:")
print(df.tail(2))

# Parts 3, 4 and 5
print("\nShape:", df.shape)
print("Columns:", df.columns.tolist())
print("\nData types:")
print(df.dtypes)

# Part 6
print("\nName and Marks:")
print(df[["Name", "Marks"]])

# Part 7
print("\nMarks greater than 80:")
print(df[df["Marks"] > 80])

# Part 8
print("\nSorted by Marks:")
print(df.sort_values("Marks", ascending=False))
