-- Write your PostgreSQL query statement below
WITH sq AS (
    SELECT D.name AS Department, E.name AS Employee, E.salary AS Salary,
        dense_rank() OVER (PARTITION BY D.name ORDER BY E.salary DESC) AS rank
    FROM Employee E
    LEFT JOIN Department D
    ON E.departmentId = D.id
)

SELECT Department, Employee, Salary FROM sq
WHERE rank <= 3