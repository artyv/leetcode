-- Write your PostgreSQL query statement below
SELECT customer_id, COUNT(*) AS count_no_trans
FROM Visits
LEFT JOIN Transactions
USING(visit_id)
GROUP BY customer_id, transaction_id
HAVING transaction_id is Null