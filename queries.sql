-- Display all employees
SELECT * FROM employees;

-- Average salary
SELECT AVG(salary) AS avg_salary FROM employees;

-- Highest paid employee
SELECT * FROM employees
WHERE salary = (SELECT MAX(salary) FROM employees);

-- Department-wise average salary
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department;

-- Employees with experience > 5 years
SELECT * FROM employees
WHERE experience > 5;
