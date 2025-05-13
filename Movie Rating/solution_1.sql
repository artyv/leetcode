-- Write your PostgreSQL query statement below
WITH user_name AS (
    SELECT name FROM Users
    INNER JOIN MovieRating
    USING(user_id)
    GROUP BY user_id, name
    ORDER BY COUNT(user_id) DESC, name ASC
    LIMIT 1
),

    movie_title AS(
    SELECT title FROM Movies
    INNER JOIN MovieRating
    USING(movie_id)
    WHERE TO_CHAR(created_at,'YYYY-MM-DD') BETWEEN '2020-02-01' AND '2020-02-29'
    GROUP BY movie_id, title
    ORDER BY AVG(rating) DESC, title ASC
    LIMIT 1
)

SELECT name AS results FROM user_name
UNION ALL
SELECT title FROM movie_title
