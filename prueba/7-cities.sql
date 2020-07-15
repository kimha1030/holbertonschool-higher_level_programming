-- Task 7
-- Create database hbtn_0d_usa and the table cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (id INT UNIQUE AUTO_INCREMENT NOT NULL, state_id INT NOT NULL, name VARCHAR(256) NOT NULL, PRIMARY KEY (id), FOREIGN KEY (state_id) REFERENCES states (id));
INSERT INTO cities (state_id, name) VALUES (1, 'San Francisco'), (1, 'San Jose'), (2, 'Page'), (3, 'Paris'), (3, 'Houston'), (3, 'Dallas');
