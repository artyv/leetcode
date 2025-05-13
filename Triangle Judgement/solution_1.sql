-- Write your PostgreSQL query statement below
SELECT *,
CASE (x < y + z AND y < x + z AND z < x + y)
    WHEN True THEN 'Yes'
    WHEN False THEN 'No'
END AS triangle
FROM Triangle