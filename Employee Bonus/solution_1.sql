-- Write your PostgreSQL query statement below
SELECT name, bonus FROM Employee
LEFT OUTER JOIN Bonus
USING(empID)
WHERE bonus is NULL or bonus < 1000