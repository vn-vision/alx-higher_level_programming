-- script that lists all the cities of California in database hbtn_0d_usa
-- the states table contain one record where name = California
SELECT * FROM cities WHERE state_id = (SELECT id FROM states WHERE name='California') ORDER BY id ASC;
