-- Task 102
-- Top 3 of cities temperature between July and August
SELECT FIRST 3 city, AVG(value) AS avg_temp FROM temperatures WHERE month BETWEEN 1 AND 8 GROUP BY city ORDER BY avg_temp DESC;
