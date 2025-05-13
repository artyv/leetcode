-- Write your PostgreSQL query statement below
SELECT DISTINCT P1.product_id, COALESCE(P2.price, 10) AS price
FROM Products P1
LEFT JOIN 
    (SELECT DISTINCT product_id, 
        LAST_VALUE(new_price) OVER(PARTITION BY product_id ORDER BY change_date RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS price
    FROM Products
    WHERE change_date <= '2019-08-16') P2
ON P1.product_id = P2.product_id