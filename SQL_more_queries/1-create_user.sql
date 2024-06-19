-- Creates the user user_0d_1 with all privileges if it does not already exist.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grants all privileges to the user user_0d_1.
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Apply the changes.
FLUSH PRIVILEGES;
