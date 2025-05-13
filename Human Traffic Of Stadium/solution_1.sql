-- Write your PostgreSQL query statement below
WITH sq AS (
    SELECT * FROM Stadium WHERE people >= 100
),
sq1 AS (
    SELECT id, visit_date, people,
        ROW_NUMBER() OVER (ORDER BY id) AS cur,
        LAG(id, 1) OVER (ORDER BY id) AS prev1,
        LAG(id, 2) OVER (ORDER BY id) AS prev2,
        LEAD(id, 1) OVER (ORDER BY id) AS next1,
        LEAD(id, 2) OVER (ORDER BY id) AS next2
    FROM sq 
)

SELECT id, visit_date, people
FROM sq1
WHERE id = prev1 + 1 AND prev1 = prev2 + 1 OR
    id + 1 = next1 AND next1 + 1 = next2 OR
    id = prev1 + 1 AND id + 1 = next1