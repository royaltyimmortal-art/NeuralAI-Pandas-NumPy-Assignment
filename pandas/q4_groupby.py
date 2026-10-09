import pandas as pd

data = {
    "Employee": ["A", "B", "C", "D", "E", "F", "G", "H"],
    "Department": ["CS", "CS", "IT", "IT", "CS", "IT", "HR", "HR"],
    "Salary": [50000, 60000, 55000, 65000, 70000, 75000, 40000, 45000],
    "Experience": [2, 4, 3, 5, 6, 7, 1, 2]
}

df = pd.DataFrame(data)
department_groups = df.groupby("Department")

average_salary = department_groups["Salary"].mean()
maximum_salary = department_groups["Salary"].max()
minimum_salary = department_groups["Salary"].min()
average_experience = department_groups["Experience"].mean()
employee_count = department_groups.size()

print("Average salary for each department:")
print(average_salary)

print("\nMaximum salary for each department:")
print(maximum_salary)

print("\nMinimum salary for each department:")
print(minimum_salary)

print("\nAverage experience for each department:")
print(average_experience)

print("\nDepartment with the highest average salary:")
print(average_salary.idxmax())

print("\nEmployee count in each department:")
print(employee_count)

print("\nDepartments sorted by average salary:")
print(average_salary.sort_values(ascending=False))
