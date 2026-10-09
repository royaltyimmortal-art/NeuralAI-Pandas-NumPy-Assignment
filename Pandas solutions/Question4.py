import pandas as pd

data = {"Employee": ["A", "B", "C", "D", "E", "F", "G", "H"], "Department": ["CS", "CS", "IT", "IT", "CS", "IT", "HR", "HR"], "Salary": [50000, 60000, 55000, 65000, 70000, 75000, 40000, 45000], "Experience": [2, 4, 3, 5, 6, 7, 1, 2]}
df = pd.DataFrame(data)
grouped = df.groupby("Department")

#part 1
average_salary = grouped["Salary"].mean()
print(average_salary)

#part 2
print(grouped["Salary"].max())

#part 3
print(grouped["Salary"].min())

#part 4
print(grouped["Experience"].mean())

#part 5
print(average_salary.idxmax())

#part 6
print(grouped["Employee"].count())

#part 7
print(average_salary.sort_values(ascending=False))
