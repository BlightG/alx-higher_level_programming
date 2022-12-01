-- a script that lists all Comedy shows in the database hbtn_0d_tvshows
SELECT tv_shows.title FROM tv_shows
RIGHT JOIN tv_show_genres
ON tv_show_genres.genre_id = '5' AND tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title IS NOT NULL
ORDER BY tv_shows.title ASC;
