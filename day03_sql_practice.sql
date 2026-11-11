
-- Day 03: SQL Practice
-- Topics: GROUP BY, HAVING, ORDER BY, Aggregate Functions

-- Create employees table
CREATE TABLE employees (
    employee_id INT,
    employee_name VARCHAR(50),
    department VARCHAR(50),
    salary INT
);

-- Insert sample records
INSERT INTO employees VALUES
(1, 'Anita', 'IT', 75000),
(2, 'Rahul', 'HR', 55000),
(3, 'Priya', 'IT', 85000),
(4, 'Sam', 'Finance', 60000),
(5, 'John', 'HR', 50000),
(6, 'Maya', 'Finance', 70000),
(7, 'Rita', 'IT', 90000);

-- 1. Display all employees
SELECT * FROM employees;

-- 2. Find the average salary
SELECT AVG(salary) AS average_salary
FROM employees;

-- 3. Count employees in each department
SELECT department, COUNT(*) AS total_employees
FROM employees
GROUP BY department;

-- 4. Find the highest salary in each department
SELECT department, MAX(salary) AS highest_salary
FROM employees
GROUP BY department;

-- 5. Display departments with average salary above 60000
SELECT department, AVG(salary) AS average_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 60000;

-- 6. Sort employees by salary (highest first)
SELECT *
FROM employees
ORDER BY salary DESC;

-- 7. Find departments with more than 2 employees
SELECT department, COUNT(*) AS total_employees
FROM employees
GROUP BY department
HAVING COUNT(*) > 2;
