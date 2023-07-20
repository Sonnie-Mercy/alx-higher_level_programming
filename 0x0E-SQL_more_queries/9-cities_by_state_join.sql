-- Database name USE hbtn_0d_usa; list all cities with corresp state names
SELECT cities.id, cities.name, states.name
FROM cities cities
INNER JOIN states states ON cities.state_id = states.id
ORDER BY cities.id ASC;
