CREATE DATABASE test;
USE test;

CREATE TABLE note(
  id INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(100),
  text VARCHAR(100),
  PRIMARY KEY (id)
);

INSERT INTO note(username,text) VALUES (foo,bar)

select scope_identity() --This should grab the ID of the newly inserted entry. Echo this back once this gets to the python script
