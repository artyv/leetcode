-- Write your PostgreSQL query statement below
WITH sq AS (
    SELECT DISTINCT P1.product_id, P2.new_price, P2.change_date
    FROM Products P1
    LEFT JOIN (SELECT product_id, new_price, change_date
            FROM Products
            WHERE change_date <= '2019-08-16'
            ) P2
    ON P1.product_id = P2.product_id
)

SELECT DISTINCT product_id, 
    COALESCE(LAST_VALUE(new_price) OVER(PARTITION BY product_id ORDER BY change_date RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING), 10) AS price
FROM sq
--GROUP BY product_id