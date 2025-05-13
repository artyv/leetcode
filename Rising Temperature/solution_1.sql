-- Write your PostgreSQL query statement below
SELECT w2.id FROM WEATHER as w1
INNER JOIN WEATHER as w2 
ON w1.recordDate = w2.recordDate - 1
AND w1.temperature < w2.temperature