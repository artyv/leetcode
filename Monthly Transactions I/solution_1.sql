-- Write your PostgreSQL query statement below
SELECT TO_CHAR(trans_date, 'yyyy-mm') AS month, country, COUNT(*) AS trans_count, 
SUM(CASE state WHEN 'approved' THEN 1 ELSE 0 END) AS approved_count,
SUM(amount) AS trans_total_amount,
SUM(CASE state WHEN 'approved' THEN amount ELSE 0 END) AS approved_total_amount
FROM Transactions
GROUP BY month, country