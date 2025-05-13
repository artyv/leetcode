-- Write your PostgreSQL query statement below
SELECT U.user_id AS buyer_id, join_date, COUNT(t.order_id) AS orders_in_2019
FROM Users U
LEFT JOIN (SELECT order_id, buyer_id
            FROM Orders
            WHERE DATE_PART('year', order_date) = 2019) t
ON U.user_id = t.buyer_id
GROUP BY U.user_id, join_date