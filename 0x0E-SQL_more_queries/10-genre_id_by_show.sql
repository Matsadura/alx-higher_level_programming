-- Lists all shows contained in the imported database
SELECT tv_shows.titles, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genreS
ON tv_shows.id = tv_show_genres.genre_id
ORDER BY title, genre_id ASC;
