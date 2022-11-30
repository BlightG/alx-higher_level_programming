-- script that creates the table id_not_null on your MySQL server
create table if not exists id_not_null (
    id INTEGER DEFAULT 1,
    name VARCHAR(256) NOT NULL);
