-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT tv_genres.name FROM tv_genres
RIGHT JOIN tv_show_genres
ON tv_show_genres.show_id = '8' AND tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name IS NOT NULL
ORDER BY tv_genres.name ASC;
