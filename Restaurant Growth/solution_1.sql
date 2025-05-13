-- Write your PostgreSQL query statement below

WITH subquery AS (
SELECT DISTINCT visited_on, 
(CASE WHEN visited_on - 6 IN (SELECT visited_on FROM Customer) THEN
SUM(amount) OVER (ORDER BY visited_on RANGE BETWEEN '6 days' PRECEDING AND CURRENT ROW) END)
AS amount, 
(CASE WHEN visited_on - 6 IN (SELECT visited_on FROM Customer) THEN
SUM(amount) OVER (ORDER BY visited_on RANGE BETWEEN '6 days' PRECEDING AND CURRENT ROW) END) AS average_amount
FROM Customer
)

SELECT visited_on, amount, ROUND(average_amount/7::numeric, 2) as average_amount FROM subquery
WHERE amount IS NOT NULL