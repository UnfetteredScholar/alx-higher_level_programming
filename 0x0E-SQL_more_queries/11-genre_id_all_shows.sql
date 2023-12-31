-- Lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
-- If a show doesn’t have a genre, display NULL

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT OUTER JOIN tv_show_genres
ON tv_shows.id=show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
