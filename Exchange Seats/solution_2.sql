-- Write your PostgreSQL query statement below
SELECT 
CASE
    WHEN MOD(id, 2) = 1 AND id != (SELECT COUNT(*) FROM Seat) THEN id + 1
    WHEN MOD(id, 2) = 0 AND id != (SELECT COUNT(*) FROM Seat) THEN id - 1
    ELSE id
END as id, student
FROM Seat
ORDER BY id