-- Write your PostgreSQL query statement below
SELECT request_at AS "Day",
    ROUND(COUNT(id) FILTER(WHERE status ILIKE 'cancelled%') /COUNT(id)::DECIMAL, 2) AS "Cancellation Rate"
FROM Trips
WHERE client_id IN (SELECT users_id FROM Users WHERE banned = 'No')
    AND driver_id IN (SELECT users_id FROM Users WHERE banned = 'No')
    AND request_at::DATE BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY 1