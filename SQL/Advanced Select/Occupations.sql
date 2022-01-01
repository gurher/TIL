
SELECT MIN(doctor), MIN(professor), MIN(singer), MIN(actor)
FROM
    (
    SELECT
    ROW_NUMBER() OVER (PARTITION BY occupation order by name) rn, 
    IF(occupation = 'Doctor', name,NULL) AS doctor
    , IF(occupation = 'Professor', name,NULL) AS professor
    , IF(Occupation = 'Singer', name,NULL) AS singer
    , IF(Occupation = 'Actor', name,NULL) AS actor
    FROM occupations
        ) X
GROUP BY rn
ORDER BY rn;

