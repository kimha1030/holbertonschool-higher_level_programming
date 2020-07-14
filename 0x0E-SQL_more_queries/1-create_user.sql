-- Task 1
-- If the user exists, delete and then, create new user with all privileges on localhost.
DROP USER 'user_0d_1'@'localhost';
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL ON * . * TO 'user_0d_1'@'localhost';
