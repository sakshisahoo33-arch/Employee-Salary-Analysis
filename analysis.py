import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/employees.csv")

avg_salary = df['salary'].mean()
print("Average Salary:", avg_salary)

max_salary = df['salary'].max()
print("Highest Salary:", max_salary)

dept_salary = df.groupby('department')['salary'].mean()
print("\nDepartment-wise Salary:\n", dept_salary)

print("\nCorrelation:\n", df[['experience', 'salary']].corr())

plt.figure()
plt.hist(df['salary'])
plt.title("Salary Distribution")
plt.savefig("../screenshots/histogram.png")

plt.figure()
dept_salary.plot(kind='bar')
plt.title("Department Salary Comparison")
plt.savefig("../screenshots/bar_chart.png")

plt.figure()
plt.scatter(df['experience'], df['salary'])
plt.title("Experience vs Salary")
plt.savefig("../screenshots/scatter_plot.png")

plt.show()
