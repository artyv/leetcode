-- Write your PostgreSQL query statement below
SELECT unique_id, name FROM Employees
FULL OUTER JOIN EmployeeUNI
USING(id)
