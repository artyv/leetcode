-- Write your PostgreSQL query statement below
WITH first_logins AS (
    SELECT player_id, MIN(event_date) AS first_login_date
    FROM Activity
    GROUP BY player_id
), 
next_day_logins AS (
    SELECT F.player_id
    FROM first_logins F
    JOIN Activity A
    ON F.player_id = A.player_id AND A.event_date = INTERVAL '1 day' + F.first_login_date
)

SELECT ROUND(COUNT(DISTINCT next_day_logins.player_id)/COUNT(DISTINCT Activity.player_id)::DECIMAL, 2) AS fraction
FROM Activity, next_day_logins