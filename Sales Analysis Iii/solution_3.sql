-- Write your PostgreSQL query statement below
WITH sq AS (
    SELECT product_id
    FROM Sales
    WHERE sale_date NOT BETWEEN '2019-01-01' AND '2019-04-01'
)


SELECT product_id, product_name
FROM Product
WHERE product_id NOT IN (SELECT * FROM sq) AND product_id IN (SELECT product_id FROM Sales)