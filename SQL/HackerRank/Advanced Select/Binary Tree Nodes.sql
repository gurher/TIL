SELECT
    N, 
    ( CASE 
        WHEN P IS NULL THEN 'Root' 
        WHEN N NOT IN (SELECT DISTINCT P 
                       FROM bst  
                       WHERE P IS NOT NULL) THEN 'Leaf' 
        ELSE 'Inner' END ) AS NodeType 
FROM bst 
ORDER BY N;




-- SELECT 
--     bst.N
--     , CASE WHEN 
-- FROM bst
-- LEFT JOIN bst1
-- ON bst.N = bst.P
