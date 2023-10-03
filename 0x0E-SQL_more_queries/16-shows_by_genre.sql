-- a script that lists all shows, and all genres for show, from the database
SELECT s.title, g.name FROM tv_shows s
LEFT JOIN tv_show_genres sg ON sg.show_id = s.id
LEFT JOIN tv_genres g ON sg.genre_id = g.id
ORDER BY s.title ASC, g.name ASC;
