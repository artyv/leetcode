-- Write your PostgreSQL query statement below
SELECT customer_id, COUNT(*) AS count_no_trans
FROM Visits
LEFT JOIN Transactions
USING(visit_id)
WHERE transaction_id is Null
GROUP BY customer_id