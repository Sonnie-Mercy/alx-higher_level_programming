-- Lists all genres of the show Dexter in the database.
SELECT genre.`name`
  FROM `tv_genres` AS genre
       INNER JOIN `tv_show_genres` AS show
       ON genre.`id` = show.`genre_id`

       INNER JOIN `tv_shows` AS tv_shows
       ON tv_shows.`id` = show.`show_id`
       WHERE t.`title` = "Dexter"
 ORDER BY genre.`name`;
