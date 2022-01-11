
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
--     hackers.hacker_id
--     , hackers.name
--     , COUNT(*) AS challenges_created
-- FROM hackers
-- LEFT JOIN challenges 
--     ON hackers.hacker_id = challenges.hacker_id
-- GROUP BY hackers.hacker_id, hackers.name
-- HAVING challenges_created IN (SELECT challenges_created
--                               FROM (SELECT hacker_id
--                                         , COUNT(*) AS challenges_created
--                                     FROM challenges
--                                     GROUP BY challenges.hacker_id) sub2
--                               GROUP BY challenges_created
--                               HAVING COUNT(*) = 1)
--     OR challenges_created = (SELECT MAX(challenges_created)
--                              FROM (SELECT COUNT(*) AS challenges_created
--                                    FROM challenges
--                                    GROUP BY challenges.hacker_id) sub1)
-- ORDER BY challenges_created DESC, hackers.hacker_id
