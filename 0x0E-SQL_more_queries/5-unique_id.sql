-- script that creates the table unique_id on your MySQL server
create table if not exists unique_id (
    id INTEGER DEFAULT 1 UNIQUE,
    name VARCHAR(256) NOT NULL);
