-- Lists all shows contained in the imported database
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows, tv_show_genres
WHERE tv_shows.id = tv_show_genres.show_id
ORDER BY title ASC, genre_id ASC;
