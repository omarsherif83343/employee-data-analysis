import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

r_csv = pd.read_csv("C:\\employees_data.csv")
#Cleaning Data

r_csv.dropna(inplace=True)
r_csv.drop_duplicates(inplace=True)

#Analysis

total_salary = r_csv["Salary"].sum()
print(total_salary)


avg_salary = r_csv["Salary"].mean()
print(avg_salary)


max_salary = r_csv["Salary"].max()
print(max_salary)

min_salary = r_csv["Salary"].min()
print(min_salary)

count_employees = r_csv.groupby("Department")["Employee_ID"].count()

average_salary_department = r_csv.groupby("Department")["Salary"].mean()
print(average_salary_department)
print(average_salary_department.idxmax())

city_count = r_csv.groupby("City")["Employee_ID"].count()
print(city_count.idxmax())

#Charts

count_employees.plot(kind='bar')
plt.title("Number of Employee by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employee")
plt.show()


average_salary_department.plot(kind='bar')
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.show()


city_count.plot(kind='pie')
plt.title("Employee Distribution by City")
plt.show()

