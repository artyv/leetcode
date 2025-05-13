-- Write your PostgreSQL query statement below
SELECT query_name, ROUND(AVG(rating/position::NUMERIC), 2) AS quality, 
ROUND(100*SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END)/COUNT(*)::NUMERIC, 2) AS poor_query_percentage
FROM Queries
GROUP BY query_name