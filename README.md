- initial create schema
CREATE DATABSE numino;

- initial create table
CREATE TABLE numino.student (
  id INT NOT NULL AUTO_INCREMENT,
  first_name VARCHAR(45) NOT NULL,
  last_name VARCHAR(45) NOT NULL,
  gender VARCHAR(10) NOT NULL,
  email VARCHAR(45) NOT NULL,
  country VARCHAR(30) NOT NULL,
  mobile VARCHAR(45) NOT NULL,
  PRIMARY KEY (id));

- insert into users table
INSERT INTO numino.student(first_name, last_name, gender, email, country, mobile)
VALUES("Allister", "Gomes", "Male", "alibaba@new.com", "India", "8668713597");

- fetch all
SELECT * FROM users;

- Specific query
SELECT * FROM users WHERE user_name = 'Allister';
