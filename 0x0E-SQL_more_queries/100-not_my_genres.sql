-- Task 100
-- Lists all genres not linked to the show Dexter
SELECT tv_genres.name AS name FROM tv_genres 
WHERE tv_genres.id NOT IN
(SELECT tv_show_genres.genre_id FROM tv_shows
INNER JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter')
GROUP BY name
ORDER BY name ASC;
