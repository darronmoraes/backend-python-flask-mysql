- initial create schema
CREATE DATABSE flaskapp;

- initial create table
CREATE TABLE users(
    user_name varchar(20),
    email varchar(40)
);

- insert into users table
INSERT INTO users(user_name, email) VALUES("darron", "darron@gmail.com");

- fetch all
SELECT * FROM users;

- Specific query
SELECT * FROM users WHERE user_name = 'darron';