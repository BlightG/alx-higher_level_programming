-- a script that creates the database hbtn_0d_usa and the table cities
CREATE database if not exists hbtn_0d_usa;
USE hbtn_0d_usa
create table if not exists cities (
    id INT PRIMARY KEY AUTO_INCREMENT,
    state_id INT NOT NULL ,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id));
