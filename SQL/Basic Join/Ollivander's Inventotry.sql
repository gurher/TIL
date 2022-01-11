
SELECT 
    w.ID
    , P.AGE
    , m.coins_needed
    , w.power 
FROM (
        SELECT 
        code 
        , MIN(coins_needed) AS coins_needed
        , power 
        FROM wands 
        GROUP BY code, power
        
        ) AS m 
LEFT JOIN wands AS w 
    ON w.code = m.code 
    AND w.power = m.power 
    AND w.coins_needed = m.coins_needed 
LEFT JOIN wands_property AS p 
    ON p.code = w.code 
WHERE p.is_evil = 0 
ORDER BY w.power DESC, p.age DESC
