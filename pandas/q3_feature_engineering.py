import pandas as pd

data = {
    "Name": ["A", "B", "C", "D", "E", "F"],
    "Math": [80, 60, 90, 70, 85, 55],
    "Science": [75, 65, 95, 72, 80, 60],
    "English": [85, 70, 88, 75, 90, 50]
}

df = pd.DataFrame(data)

# Parts 1, 2 and 3
df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)
df["Total"] = df[["Math", "Science", "English"]].sum(axis=1)
df["Passed"] = df["Average"] >= 60

# Part 4
print("Highest average student:")
print(df.loc[df["Average"].idxmax()])

# Part 5
print("\nAverage greater than or equal to 80:")
print(df[df["Average"] >= 80])

# Part 6
print("\nSorted by Average:")
print(df.sort_values("Average", ascending=False))

# Part 7
print("\nOverall average:", df["Average"].mean())

# Part 8
print("\nName, Average and Passed:")
print(df[["Name", "Average", "Passed"]])
