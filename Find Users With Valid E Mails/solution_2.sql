-- Write your PostgreSQL query statement below
SELECT * FROM Users
WHERE mail SIMILAR TO '[A-Za-z][A-Za-z0-9_.-]*@leetcode.com'
