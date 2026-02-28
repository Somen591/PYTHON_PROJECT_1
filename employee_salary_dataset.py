import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = {
    'Employee': ['Amit', 'Riya', 'Rahul', 'Priya', 'Suman', 'Ankit', 'Neha', 'Rohit'],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'HR', 'Finance', 'IT', 'HR'],
    'Salary': [50000, 42000, 60000, 55000, 45000, 52000, 65000, 40000],
    'Experience_Years': [2, 1, 4, 3, 2, 3, 5, 1]
}
df= pd.DataFrame ({
    'Employee': ['Amit', 'Riya', 'Rahul', 'Priya', 'Suman', 'Ankit', 'Neha', 'Rohit'],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'HR', 'Finance', 'IT', 'HR'],
    'Salary': [50000, 42000, 60000, 55000, 45000, 52000, 65000, 40000],
    'Experience_Years': [2, 1, 4, 3, 2, 3, 5, 1]
})

# avg_salary_dpt = df.groupby('Department').agg({'Salary' : 'mean'})
# print(avg_salary_dpt)
# print("department pays the highest avg salary",df.sort_values(by=avg_salary_dpt,ascending=False))

# emp_per_dept = df.groupby('Department').agg({'Employee':'size'})
# print(type(emp_per_dept))
# array = np.array([emp_per_dept])
# print(array)

# dept_count = df['Department'].value_counts()
# print(dept_count)

# import matplotlib.pyplot as plt

# dept_count.plot(kind='bar')
# plt.xlabel('Department')
# plt.ylabel('Number of Employees')
# plt.title('Employees per Department')
# plt.show()

df['salary_per_year'] = df['Salary'] / df['Experience_Years']
# print(df)
print("highest value employee",df.max('salary_per_year'))