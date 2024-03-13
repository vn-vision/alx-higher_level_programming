-- this script creates user user_0d_1
-- the user has all privileges -- password set to user_0d_pwd
-- if user already exists return
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- don't forget to reload grant tables to ensure new images are in effect
FLUSH PRIVILEGES;
