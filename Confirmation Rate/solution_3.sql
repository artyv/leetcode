-- Write your PostgreSQL query statement below
with sub AS (SELECT user_id,
CASE
    WHEN action='confirmed' THEN 1
    ELSE 0
END AS cat1,
COUNT(*) as cat2
FROM Confirmations
GROUP BY user_id, action)

SELECT s.user_id, ROUND(SUM(COALESCE(sub.cat1, 0))/COUNT(*)::NUMERIC, 2) as confirmation_rate
FROM Signups as s
FULL OUTER JOIN sub
ON s.user_id = sub.user_id
GROUP BY s.user_id
