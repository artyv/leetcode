-- Write your PostgreSQL query statement below
WITH sq AS (
    SELECT income,
        CASE
            WHEN income < 20000 THEN 'Low Salary'
            WHEN income <= 50000 THEN 'Average Salary'
            ELSE 'High Salary'
            END AS category
    FROM Accounts
), categories AS (
    SELECT * FROM (VALUES ('Low Salary'), ('Average Salary'), ('High Salary')) AS c(category)
)

SELECT c.category, COALESCE(COUNT(sq.income), 0) AS accounts_count
FROM categories c
LEFT JOIN sq
USING(category)
GROUP BY c.category