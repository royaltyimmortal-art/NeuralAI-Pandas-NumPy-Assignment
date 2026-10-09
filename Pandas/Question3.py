import pandas as pd

data = {"Name": ["A", "B", "C", "D", "E", "F"], "Math": [80, 60, 90, 70, 85, 55], "Science": [75, 65, 95, 72, 80, 60], "English": [85, 70, 88, 75, 90, 50]}
df = pd.DataFrame(data)

#part 1
df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)

#part 2
df["Total"] = df[["Math", "Science", "English"]].sum(axis=1)

#part 3
df["Passed"] = df["Average"] >= 60

#part 4
print(df.loc[df["Average"].idxmax()])

#part 5
print(df[df["Average"] >= 80])

#part 6
print(df.sort_values("Average", ascending=False))

#part 7
print(df["Average"].mean())

#part 8
print(df[["Name", "Average", "Passed"]])
