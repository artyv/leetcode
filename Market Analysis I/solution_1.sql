-- Write your PostgreSQL query statement below
SELECT U.user_id AS buyer_id, join_date, COUNT(O.order_id) AS orders_in_2019
FROM Users U
LEFT JOIN Orders O
ON U.user_id = O.buyer_id AND DATE_PART('year', order_date) = 2019
GROUP BY U.user_id, join_date