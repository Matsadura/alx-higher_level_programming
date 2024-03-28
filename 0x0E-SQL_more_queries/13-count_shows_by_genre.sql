SELECT tv_genre.name AS genre,
COUNT(tv_genre.name) AS number_of_shows
FROM tv_genres
LEFT JOIN tv_shows_genre
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
