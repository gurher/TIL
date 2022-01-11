
 temp AS (
        SELECT 
            c.hacker_id AS hacker_id
            , h.name AS name
            , COUNT(DISTINCT c.challenge_id) AS challenges_created
        FROM challenges c
        LEFT JOIN hackers h
            ON c.hacker_id = h.hacker_id
        GROUP BY 1, 2
        ORDER BY 3
    )
    
SELECT 
    hacker_id
    , name
    , challenges_created
FROM temp
GROUP BY 1,2,3
HAVING COUNT(challenges_created) > 1
    AND 


-- WITH counter AS (
--     SELECT 
--         h.hacker_id
--         , h.name
--         , COUNT(*) AS challenges_created
--     FROM challenges c
--     LEFT JOIN hackers h 
--         ON c.hacker_id = h.hacker_id
--     GROUP BY h.hacker_id, h.name
--                 )
    
-- SELECT 
--     hacker_id
--     , name
--     , challenges_created
-- FROM counter
-- WHERE challenges_created = (
--                             SELECT 
--                             MAX(challenges_created) 
--                             FROM counter
--                             )
--     OR challenges_created IN (
--                             SELECT challenges_created
--                             FROM counter
--                             GROUP BY challenges_created
--                             HAVING COUNT(*) = 1
--                             )
-- ORDER BY challenges_created DESC, hacker_id

