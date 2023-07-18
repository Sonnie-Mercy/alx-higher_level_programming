-- import dump and convert temperature to Farenheit
SELECT city, AVG(value * 9/5) + 32) FROM temperatures GROUP BY city ORDER BY 2 DESC;
