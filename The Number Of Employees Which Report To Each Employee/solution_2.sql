-- Write your PostgreSQL query statement below
WITH sq AS (
    SELECT t1.employee_id, t1.name, t2.employee_id AS managed, t2.age
    FROM Employees t1
    INNER JOIN Employees t2
    ON t1.employee_id = t2.reports_to
)

SELECT employee_id, name, COUNT(managed) AS reports_count,
    ROUND(AVG(age),0) AS average_age
FROM sq
GROUP BY employee_id, name
ORDER BY 1