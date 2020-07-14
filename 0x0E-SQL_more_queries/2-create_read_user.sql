-- Task 2
-- Create DB and user with select privilege
DROP DATABASE IF EXISTS hbtn_0d_2;
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
DROP USER IF EXISTS 'user_0d_2'@'localhost';
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2. * TO 'user_0d_2'@'localhost';
