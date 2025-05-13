-- Write your PostgreSQL query statement below
WITH sq AS (
    SELECT * FROM Stadium WHERE people >= 100
),
sq1 AS (
    SELECT id, visit_date, people,
        id - ROW_NUMBER() OVER (ORDER BY id) AS grp
    FROM sq 
)

SELECT id, visit_date, people
FROM sq1
WHERE grp IN (
    SELECT grp 
    FROM sq1 
    GROUP BY grp 
    HAVING COUNT(*) >= 3
)
ORDER BY id;