-- Write your PostgreSQL query statement below
UPDATE Users
SET name = CONCAT(UPPER(LEFT(name, 1)), LOWER(RIGHT(name, -1)))
RETURNING *