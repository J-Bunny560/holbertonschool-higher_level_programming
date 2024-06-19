-- Creates the database hbtn_0d_2 and the user user_0d_2
-- The user_0d_2 has SELECT privilege on hbtn_0d_2 with password user_0d_2_pwd

-- Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS `hbtn_0d_2`;

-- Create the user if it does not exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege on the database to the user
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';

-- Apply the changes
FLUSH PRIVILEGES;