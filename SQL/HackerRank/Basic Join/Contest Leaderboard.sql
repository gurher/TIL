SELECT 
    score_board.hacker_id AS hacker_ids,
    Hackers.name,
    SUM(score_board.score) AS scores
FROM (SELECT 
        hacker_id,
        challenge_id,
        MAX(score) score
    FROM Submissions
    GROUP BY 1,2) score_board
LEFT JOIN Hackers
    ON Hackers.hacker_id = score_board.hacker_id
GROUP BY 1,2   
HAVING scores > 0
ORDER BY scores DESC,hacker_ids ASC 
