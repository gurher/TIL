
WITH history AS (
SELECT user_id, song_id, song_plays
FROM songs_history

UNION ALL

SELECT user_id, song_id, COUNT(song_id) AS song_plays
FROM songs_weekly
WHERE listen_time <= DATE('08/05/2022')
GROUP BY user_id, song_id
)

SELECT user_id, song_id, SUM(song_plays) AS song_count
FROM history
GROUP BY user_id, song_id
ORDER BY song_count DESC;