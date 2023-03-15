-- lists all shows contained in hbtn_0d_tvshows without a genre linked
SELECT s.title, sg.genre_id
FROM tv_shows s
RIGHT JOIN tv_show_genres sg ON s.id = sg.show_id
WHERE sg.show_id is NULL
ORDER BY s.title, sg.genre_id;
