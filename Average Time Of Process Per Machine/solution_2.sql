-- Write your PostgreSQL query statement below
SELECT machine_id, ROUND(SUM(time)::NUMERIC/(COUNT(*)/2), 3) AS processing_time FROM
(SELECT machine_id,
CASE activity_type
WHEN 'start' THEN timestamp*(-1)
WHEN 'end' THEN timestamp
END as time
FROM Activity)
GROUP BY machine_id