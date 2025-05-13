-- Write your PostgreSQL query statement below
WITH sq AS (
    SELECT name FROM SalesPerson
    LEFT JOIN Orders
    USING (sales_id)
    WHERE com_id IN (SELECT com_id FROM Company WHERE name = 'RED')
)

SELECT name FROM SalesPerson
WHERE name NOT IN (SELECT * FROM sq)