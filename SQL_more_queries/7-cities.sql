--  creates the database hbtn_0d_usa and the table cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- create tabel with freign key
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
-- state_id column in the current table is a foreign key that refers to the id column in the states with primary key
FOREIGN KEY (state_id) REFERENCES states(id)
);