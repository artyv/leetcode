SELECT S.product_id, product_name
FROM Sales S
INNER JOIN Product
USING (product_id)
GROUP BY product_id, product_name
HAVING MIN(sale_date) >= '2019-01-01' AND MAX(sale_date) < '2019-04-01'