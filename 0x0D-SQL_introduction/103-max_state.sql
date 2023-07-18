-- dispalys the max temperature of each state ordered by State Name
SELECT state, MAX(value) FROM temperature GROUP BY state ORDER BY state;
