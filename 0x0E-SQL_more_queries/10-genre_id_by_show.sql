-- lists all shows in hbtn_0d_tvshows with at least one genre linked.
SELECT s.title, sg.genre_id
FROM tv_shows s
INNER JOIN tv_show_genres sg ON s.id = sg.show_id
ORDER BY s.title ASC, sg.genre_id ASC;
