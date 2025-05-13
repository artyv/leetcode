-- Write your PostgreSQL query statement below
SELECT person_name 
FROM (SELECT person_name, SUM(weight) OVER (ORDER BY turn) FROM Queue)
WHERE sum <= 1000
ORDER BY sum DESC
LIMIT 1
