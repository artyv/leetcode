-- Write your PostgreSQL query statement below
SELECT s.user_id, COALESCE(ROUND(AVG(CASE WHEN action = 'confirmed' THEN 1 ELSE 0 END), 2), 0) as confirmation_rate
FROM Signups as s
LEFT JOIN Confirmations
USING(user_id)
GROUP BY user_id
