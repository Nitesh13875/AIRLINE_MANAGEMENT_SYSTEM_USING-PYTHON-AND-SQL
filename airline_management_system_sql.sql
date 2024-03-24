-- Create database
CREATE DATABASE IF NOT EXISTS AMS;

-- Use the database
USE AMS;

-- Create flights table
CREATE TABLE IF NOT EXISTS flights (
    id INT AUTO_INCREMENT PRIMARY KEY,
    flight_number VARCHAR(10) NOT NULL,
    departure_airport VARCHAR(255) NOT NULL,
    arrival_airport VARCHAR(255) NOT NULL,
    departure_time DATETIME NOT NULL,
    arrival_time DATETIME NOT NULL
);

-- Create passengers table
CREATE TABLE IF NOT EXISTS passengers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    email VARCHAR(255) NOT NULL,
    flight_id INT NOT NULL,
    seat_number VARCHAR(10) NOT NULL,
    FOREIGN KEY (flight_id) REFERENCES flights(id)
);

-- Create crew_members table
CREATE TABLE IF NOT EXISTS crew_members (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    position VARCHAR(255) NOT NULL,
    flight_id INT NOT NULL,
    FOREIGN KEY (flight_id) REFERENCES flights(id)
);

-- Create luggage table
CREATE TABLE IF NOT EXISTS luggage (
    id INT AUTO_INCREMENT PRIMARY KEY,
    weight FLOAT NOT NULL,
    passenger_id INT NOT NULL,
    fine FLOAT DEFAULT 0,
    FOREIGN KEY (passenger_id) REFERENCES passengers(id)
);

-- Create passenger_info table
CREATE TABLE IF NOT EXISTS passenger_info (
    id INT AUTO_INCREMENT PRIMARY KEY,
    passenger_id INT NOT NULL,
    food_preference VARCHAR(255),
    is_senior_citizen BOOLEAN,
    FOREIGN KEY (passenger_id) REFERENCES passengers(id)
);

-- Create payments table
CREATE TABLE IF NOT EXISTS payments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    payment_date DATETIME NOT NULL,
    amount FLOAT NOT NULL,
    payment_method VARCHAR(255) NOT NULL,
    passenger_id INT NOT NULL,
    FOREIGN KEY (passenger_id) REFERENCES passengers(id)
);
-- Insert data into flights table
INSERT INTO flights (flight_number, departure_airport, arrival_airport, departure_time, arrival_time)
VALUES 
    ('AI101', 'Mumbai', 'Delhi', '2023-05-01 09:00:00', '2023-05-01 11:00:00'),
    ('AI102', 'Delhi', 'Mumbai', '2023-05-01 14:00:00', '2023-05-01 16:00:00');

-- Insert data into passengers table
INSERT INTO passengers (name, age, email, flight_id, seat_number)
VALUES 
    ('Nitesh Mishra', 20, 'Nitesh13875@gmail.com', 1, 'A1'),
    ('Dhruvi Khimasiya', 20, 'Dhruvik@gmail.com', 1, 'A2'),
    ('Rohit Pal', 20, 'prohit@gmail.com', 2, 'B1');

-- Insert data into crew_members table
INSERT INTO crew_members (name, position, flight_id)
VALUES 
    ('Tushar Gupta', 'Pilot', 1),
    ('Gaurav Malik', 'Co-Pilot', 1),
    ('Mansi Dongre', 'Flight Attendant', 2),
    ('Srushti Mogaveera', 'Flight Attendant', 2);

-- Insert data into passenger_info table
INSERT INTO passenger_info (passenger_id, food_preference, is_senior_citizen)
VALUES 
    (1, 'Vegetarian', FALSE),
    (2, 'Non-vegetarian', TRUE),
    (3, 'Vegetarian', FALSE);

-- Insert data into payments table
INSERT INTO payments (payment_date, amount, payment_method, passenger_id)
VALUES 
    ('2023-05-01 10:30:00', 100.0, 'Credit Card', 1),
    ('2023-05-01 12:30:00', 200.0, 'Debit Card', 2),
    ('2023-05-01 14:30:00', 150.0, 'Cash', 3);

-- Insert data into luggage table
INSERT INTO luggage (weight, passenger_id)
VALUES 
    (8.5, 1),
    (15, 2),
    (11, 3);