-- Write your PostgreSQL query statement below

select name
FROM Employee AS E1
INNER JOIN
(SELECT managerId, COUNT(managerId) as cnt FROM Employee
GROUP BY managerId) AS E2
ON E1.id = E2.managerId
WHERE cnt >= 5
