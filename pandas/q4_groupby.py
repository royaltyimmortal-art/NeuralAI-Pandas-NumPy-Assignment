import pandas as pd

data = {
    "Employee": ["A", "B", "C", "D", "E", "F", "G", "H"],
    "Department": ["CS", "CS", "IT", "IT", "CS", "IT", "HR", "HR"],
    "Salary": [50000, 60000, 55000, 65000, 70000, 75000, 40000, 45000],
    "Experience": [2, 4, 3, 5, 6, 7, 1, 2]
}

df = pd.DataFrame(data)
grouped = df.groupby("Department")

# Part 1
average_salary = grouped["Salary"].mean()
print("Average salary:")
print(average_salary)

# Part 2
print("\nMaximum salary:")
print(grouped["Salary"].max())

# Part 3
print("\nMinimum salary:")
print(grouped["Salary"].min())

# Part 4
print("\nAverage experience:")
print(grouped["Experience"].mean())

# Part 5
print("\nDepartment with highest average salary:", average_salary.idxmax())

# Part 6
print("\nEmployee count:")
print(grouped["Employee"].count())

# Part 7
print("\nDepartments sorted by average salary:")
print(average_salary.sort_values(ascending=False))
