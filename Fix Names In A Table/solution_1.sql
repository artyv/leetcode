-- Write your PostgreSQL query statement below
WITH updated_table AS (
    UPDATE Users
    SET name = CONCAT(UPPER(LEFT(name, 1)), LOWER(RIGHT(name, -1))) 
    RETURNING *)

SELECT * FROM updated_table
ORDER BY user_id