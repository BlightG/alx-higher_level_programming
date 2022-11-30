-- a script that lists all cities contained in the database hbtn_0d_usa
select cities.id, cities.name, states.name from cities
right join states
on cities.state_id = states.id;