-- Write your PostgreSQL query statement below
with sub AS (SELECT user_id,
ROUND(SUM(CASE
    WHEN action='confirmed' THEN 1
    ELSE 0
END)/COUNT(*)::NUMERIC, 2) AS cat1
FROM Confirmations
GROUP BY user_id)

--select * from sub

SELECT s.user_id, COALESCE(sub.cat1, 0) as confirmation_rate
FROM Signups as s
LEFT JOIN sub
USING(user_id)
