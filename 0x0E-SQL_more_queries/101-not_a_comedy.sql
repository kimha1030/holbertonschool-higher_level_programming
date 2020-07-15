-- Task 101
-- Lists all shows without the genre Comedy
SELECT tv_shows.title AS title FROM tv_shows
WHERE tv_shows.id NOT IN
(SELECT tv_show_genres.show_id FROM tv_genres
INNER JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy')
GROUP BY title
ORDER BY title ASC;
