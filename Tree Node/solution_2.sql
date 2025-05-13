-- Write your PostgreSQL query statement below
SELECT id, 
    CASE
        WHEN p_id IS Null THEN 'Root'
        WHEN id NOT IN (SELECT DISTINCT p_id FROM Tree WHERE p_id IS NOT NULL) THEN 'Leaf'
        ELSE 'Inner'
    END AS type
FROM Tree