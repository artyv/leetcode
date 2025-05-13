-- Write your PostgreSQL query statement below
-- SELECT ROUND(SUM(
--     CASE
--     WHEN order_date = customer_pref_delivery_date THEN 1
--     ELSE 0
--     END)
--     /COUNT(customer_id)::DECIMAL, 2) AS immediate_percentage

select 
    round(sum(CASE
    WHEN od = pd THEN 1
    ELSE 0
    END) * 100
    /COUNT(customer_id)::DECIMAL, 2) AS immediate_percentage
from (
select customer_id, min(order_date) as od, min(customer_pref_delivery_date) as pd
FROM Delivery
GROUP BY customer_id) t
