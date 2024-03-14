-- this script creates the table unique_id
-- description int default 1 and unique, name
CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256) NOT NULL
);
