-- Write your PostgreSQL query statement below
SELECT NULLIF(
    (SELECT num FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
    ORDER BY num DESC
    LIMIT 1),
    null
) as num FROM MyNumbers
LIMIT 1

