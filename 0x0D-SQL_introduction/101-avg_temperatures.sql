-- Task 101
-- Import table in DB
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
