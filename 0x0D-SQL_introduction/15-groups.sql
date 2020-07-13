-- Task 15
-- Lists number of records with same score
SELECT COUNT(score) AS number FROM second_table GROUP BY score ORDER BY number DESC;
