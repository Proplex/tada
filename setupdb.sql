CREATE DATABASE db;
USE db;

CREATE TABLE users(
  username VARCHAR(30),
  password VARCHAR(3000)
  
);

CREATE TABLE notes(
  id INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(30),
  text VARCHAR(100),
  PRIMARY KEY (id)
);

CREATE TABLE calendar(
  id INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(30),
  text VARCHAR(100),
  date DATETIME,
  PRIMARY KEY (id)
);