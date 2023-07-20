-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT show.title, sg.genre_id
FROM tv_shows show
JOIN tv_show_genres AS sg ON show.id = sg.show_id
ORDER BY show.title ASC, sg.genre_id ASC;
