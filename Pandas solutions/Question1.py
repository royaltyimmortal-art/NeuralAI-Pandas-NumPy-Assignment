import pandas as pd

data = {"Name": ["A", "B", "C", "D", "E"], "Age": [20, 25, 22, 30, 28], "Marks": [85, 72, 90, 65, 88], "City": ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai"]}
df = pd.DataFrame(data)

#part 1
print(df.head(3))

#part 2
print(df.tail(2))

#part 3
print(df.shape)

#part 4
print(df.columns.tolist())

#part 5
print(df.dtypes)

#part 6
print(df[["Name", "Marks"]])

#part 7
print(df[df["Marks"] > 80])

#part 8
print(df.sort_values("Marks", ascending=False))
