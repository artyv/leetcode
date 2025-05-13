-- Write your PostgreSQL query statement below
SELECT * FROM Patients
WHERE conditions ILIKE 'DIAB1%' OR conditions ILIKE '% DIAB1%'