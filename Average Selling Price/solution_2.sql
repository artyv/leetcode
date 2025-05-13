-- Write your PostgreSQL query statement below
SELECT P.product_id, ROUND(SUM(P.price*U.units)/SUM(U.units)::NUMERIC, 2) as average_price FROM Prices AS P
FULL OUTER JOIN UnitsSold AS U
ON P.product_id = U.product_id 
AND U.purchase_date BETWEEN P.start_date and P.end_date
WHERE U.units is not Null
GROUP BY P.product_id