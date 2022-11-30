-- script that creates the table force_name on your MySQL server
create table if not exists force_name (
    id INTEGER,
    name VARCHAR(256) NOT NULL);
