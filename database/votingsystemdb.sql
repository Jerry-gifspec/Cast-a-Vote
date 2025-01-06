-- Create the database
CREATE DATABASE IF NOT EXISTS votingsystemdb;
USE votingsystemdb;

-- Create users table
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    aadhar VARCHAR(20) UNIQUE,
    role ENUM('voter', 'admin') NOT NULL
);

-- Create elections table
CREATE TABLE elections (
    election_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    start_date DATETIME NOT NULL,
    end_date DATETIME NOT NULL,
    status ENUM('ongoing', 'completed') DEFAULT 'ongoing'
);

-- Create positions table
CREATE TABLE positions (
    position_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    election_id INT NOT NULL,
    FOREIGN KEY (election_id) REFERENCES elections(election_id) ON DELETE CASCADE
);

-- Create candidates table
CREATE TABLE candidates (
    candidate_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    election_id INT NOT NULL,
    position_id INT NOT NULL,
    votes INT DEFAULT 0,
    FOREIGN KEY (election_id) REFERENCES elections(election_id) ON DELETE CASCADE,
    FOREIGN KEY (position_id) REFERENCES positions(position_id) ON DELETE CASCADE
);

-- Create votes table
CREATE TABLE votes (
    vote_id INT AUTO_INCREMENT PRIMARY KEY,
    voter_id INT NOT NULL,
    election_id INT NOT NULL,
    candidate_id INT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (voter_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (election_id) REFERENCES elections(election_id) ON DELETE CASCADE,
    FOREIGN KEY (candidate_id) REFERENCES candidates(candidate_id) ON DELETE CASCADE
);

-- Add sample data (optional)
-- Insert default admin
INSERT INTO users (username, email, password, role) 
VALUES ('admin', 'admin@example.com', 'hashed_password_here', 'admin');

-- Insert sample election
INSERT INTO elections (name, start_date, end_date, status) 
VALUES ('Presidential Election', '2024-01-01 09:00:00', '2024-01-02 18:00:00', 'ongoing');

-- Insert sample positions
INSERT INTO positions (name, election_id) 
VALUES ('President', 1), ('Vice President', 1);

-- Insert sample candidates
INSERT INTO candidates (name, election_id, position_id) 
VALUES 
('Candidate A', 1, 1),
('Candidate B', 1, 1),
('Candidate C', 1, 2);

-- Test complete setup
SELECT * FROM users;
SELECT * FROM elections;
SELECT * FROM positions;
SELECT * FROM candidates;
SELECT * FROM votes;
