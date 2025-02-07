-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS todo_db;

-- Use the database
USE todo_db;

-- Create the tasks table
CREATE TABLE IF NOT EXISTS tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    is_complete BOOLEAN DEFAULT false
);