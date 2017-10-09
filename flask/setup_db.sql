CREATE DATABASE db;
USE db;

CREATE TABLE users(
  username VARCHAR(100)  
);

CREATE TABLE note(
  id INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(100),
  text VARCHAR(100),
  x INT,
  y INT,
  PRIMARY KEY (id)
);

CREATE TABLE event(
  id INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(100),
  text VARCHAR(100),
  datetime DATETIME,
  PRIMARY KEY (id)
);
