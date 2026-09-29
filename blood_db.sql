CREATE DATABASE blood_db;

USE blood_db;

CREATE TABLE donor (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    blood_group VARCHAR(10) NOT NULL,
    phone VARCHAR(15) UNIQUE NOT NULL,
    city VARCHAR(100) NOT NULL,
    last_donation DATE
);