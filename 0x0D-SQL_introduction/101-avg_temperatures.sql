-- Task 101
-- Import table in DB
mysql hbtn_0c_0 < temperatures.sql
SELECT city, AVG(value) AS avg_temp FROM temperatures ORDER BY value DESC; 
