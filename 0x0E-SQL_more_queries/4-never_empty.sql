-- this script creates table id_not_null on MySQL
-- description id default 1, name
CREATE TABLE IF NOT EXISTS id_not_null (
	id INT DEFAULT 1,
	name VARCHAR(256) NOT NULL
);
