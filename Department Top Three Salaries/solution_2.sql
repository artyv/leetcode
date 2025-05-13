-- Write your PostgreSQL query statement below
WITH sq AS (
    SELECT D.name AS Department, E.name AS Employee, salary AS Salary
    FROM Employee E
    INNER JOIN Department D
    ON E.departmentId = D.id
),
sq1 AS (
    SELECT Department, Employee, Salary,
        DENSE_RANK() OVER(PARTITION BY Department ORDER BY Salary DESC) AS rank
    FROM sq
)

SELECT Department, Employee, Salary 
FROM sq1
WHERE rank <= 3