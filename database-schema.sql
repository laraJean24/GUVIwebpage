-- User Management Database Schema
-- Execute this SQL to set up the database

-- Create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS user_management_db;
USE user_management_db;

-- Drop table if exists (for fresh install)
DROP TABLE IF EXISTS users;

-- Create users table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    firstName VARCHAR(100) NOT NULL,
    lastName VARCHAR(100) NOT NULL,
    email VARCHAR(120) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    age INT DEFAULT NULL,
    dob DATE DEFAULT NULL,
    contact VARCHAR(20) DEFAULT NULL,
    address TEXT DEFAULT NULL,
    city VARCHAR(100) DEFAULT NULL,
    state VARCHAR(100) DEFAULT NULL,
    zipcode VARCHAR(10) DEFAULT NULL,
    createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_email (email),
    INDEX idx_createdAt (createdAt)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Create indexes for better performance
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_createdAt ON users(createdAt);

-- Insert sample user for testing (password: password123)
-- Email: test@example.com
-- Password Hash: $2y$10$N9qo8uLOickgx2ZMRZoMyeIjZAgcg7b3XeKeUxWdeS86E36P4/LaO
INSERT INTO users (firstName, lastName, email, password) VALUES 
('Test', 'User', 'test@example.com', '$2y$10$N9qo8uLOickgx2ZMRZoMyeIjZAgcg7b3XeKeUxWdeS86E36P4/LaO');
