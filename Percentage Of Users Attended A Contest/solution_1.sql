-- Write your PostgreSQL query statement below
SELECT contest_id, 
ROUND(100*COUNT(*)/(SELECT COUNT(*) FROM Users)::NUMERIC, 2) AS percentage
FROM Register
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC