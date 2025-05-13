-- Write your PostgreSQL query statement below
WITH sq AS (
    SELECT COUNT(*) AS count_pos
    FROM Activity A1
    JOIN Activity A2
    ON A1.player_id = A2.player_id AND A1.event_date - INTERVAL '1 day' = A2.event_date
    GROUP BY A1.player_id
)

SELECT ROUND((SELECT * FROM sq)/COUNT(DISTINCT player_id)::DECIMAL, 2) AS fraction
FROM Activity