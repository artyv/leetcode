-- -- Write your PostgreSQL query statement below
SELECT ROUND(COUNT(player_id) FILTER (WHERE date_diff = 1)::DECIMAL / COUNT(DISTINCT player_id), 2) AS fraction
FROM (
    SELECT player_id,
        event_date - FIRST_VALUE(event_date) OVER(PARTITION BY player_id ORDER BY event_date) AS date_diff
    FROM Activity
) s