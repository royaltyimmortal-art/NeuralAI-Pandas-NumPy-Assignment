import pandas as pd

data = {
    "Name": ["A", "B", "C", "D", "E", "F"],
    "Math": [80, 60, 90, 70, 85, 55],
    "Science": [75, 65, 95, 72, 80, 60],
    "English": [85, 70, 88, 75, 90, 50]
}

df = pd.DataFrame(data)

subject_columns = ["Math", "Science", "English"]

df["Average"] = df[subject_columns].mean(axis=1)
df["Total"] = df[subject_columns].sum(axis=1)
df["Passed"] = df["Average"] >= 60

print("DataFrame with Average, Total and Passed columns:")
print(df)

print("\nStudent with the highest average:")
print(df.loc[df["Average"].idxmax()])

print("\nStudents whose average is 80 or more:")
print(df[df["Average"] >= 80])

print("\nStudents sorted by average in descending order:")
print(df.sort_values(by="Average", ascending=False))

print("\nOverall average:", df["Average"].mean())

print("\nName, Average and Passed:")
print(df[["Name", "Average", "Passed"]])
