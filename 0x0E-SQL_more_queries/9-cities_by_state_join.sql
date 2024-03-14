-- a script that lists all cities containe in the database hbtn_0d_usa
-- Results must be sorted in ascending order bt cities id
-- only use one SELECT, select id and name columns from ciites table
-- name column from states table join them using state_id
SELECT cities.id, cities.name, states.name
FROM hbtn_0d_usa.cities INNER JOIN hbtn_0d_usa.states ON
cities.state_id = states.id ORDER BY cities.id ASC;
