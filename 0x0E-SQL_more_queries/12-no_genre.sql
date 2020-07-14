-- Task 12
-- Lists all shows contained in hbtn_0d_tvshows without a genre linked
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_genres 
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id 
RIGHT JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id WHERE tv_show_genres.show_id IS NULL 
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
