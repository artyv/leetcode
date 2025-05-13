-- Write your PostgreSQL query statement below
SELECT U.name, SUM(T.amount) AS balance
FROM Transactions T
LEFT JOIN Users U
USING (account)
GROUP BY U.name
HAVING SUM(T.amount) > 10000