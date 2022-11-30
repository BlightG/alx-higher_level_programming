--  a script that lists all the cities of California that can be found in the database
select cities.id, cities.name
from cities
where cities.state_id = '1';