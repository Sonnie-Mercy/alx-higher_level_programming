-- Database name USE hbtn_0d_usa; list all cities with corresp state names
SELECT cities.id, cities.name, states.name AS state_name
FROM cities
INNER JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
