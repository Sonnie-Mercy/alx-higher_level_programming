-- import dump and convert temperature to Farenheit
SELECT city, AVG(value) FROM temperatures GROUP BY city ORDER BY 2 DESC;
