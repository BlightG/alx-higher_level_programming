--  a script that creates the database hbtn_0d_usa and the table states
CREATE database if not exists hbtn_0d_usa;
USE hbtn_0d_usa
create table if not exists states (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL)
