-- Database name Carlifornia city
SELECT city.id, city.name FROM cities city INNER JOIN states state
ON city.state_id = state.id WHERE state.name = "California";
