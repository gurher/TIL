WITH table1 AS (
    SELECT 
      artists.artist_name,
      COUNT(*) counts,
      DENSE_RANK() OVER( ORDER BY COUNT(*) DESC) ranking
        
    FROM artists
    INNER JOIN songs
      ON artists.artist_id = songs.artist_id
    INNER JOIN global_song_rank AS globals
      ON songs.song_id = globals.song_id
    WHERE globals.rank < 11
    GROUP BY artist_name
    
    )
    
SELECT 
  artist_name,
  ranking
FROM table1
WHERE ranking < 6
