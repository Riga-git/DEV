CREATE DATABASE IF NOT EXISTS personstore;
USE personstore;

CREATE TABLE IF NOT EXISTS persons (
name VARCHAR(50) NOT NULL, 
firstname VARCHAR(50) NOT NULL,
street VARCHAR(255) NOT NULL,
streetNbr INT NOT NULL,
CAP CHAR(4) NOT NULL,
city VARCHAR(255) NOT NULL,
phone VARCHAR(50) NOT NULL,
CONSTRAINT persons_pk PRIMARY KEY (name, firstname));