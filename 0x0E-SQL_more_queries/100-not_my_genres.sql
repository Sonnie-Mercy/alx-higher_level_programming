-- lists all shows not linked to DEXTER in the database
SELECT g.name FROM tv_genres g WHERE g.name NOT IN (
	SELECT g.name FROM tv_genres g
	INNER JOIN tv_show_genres sg ON g.id = sg.genre_id
	INNER JOIN tv_shows s on sg.show_id = s.id
	WHERE s.title = 'Dexter'
) ORDER BY g.name ASC;
