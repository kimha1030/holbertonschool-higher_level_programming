-- Task 13
-- List name of geners and count
SELECT tv_genres.name, COUNT(tv_shows.id) AS number_of_shows FROM tv_shows 
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id 
INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
