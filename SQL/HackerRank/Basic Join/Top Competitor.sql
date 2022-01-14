
SELECT s.hacker_id, h.name
FROM submissions s
LEFT JOIN challenges c 
    ON s.challenge_id = c.challenge_id
LEFT JOIN difficulty d 
    ON c.difficulty_level = d.difficulty_level
LEFT JOIN hackers h 
    ON s.hacker_id = h.hacker_id
WHERE d.score = s.score
GROUP BY s.hacker_id, h.name
HAVING COUNT(s.challenge_id) > 1
ORDER BY COUNT(s.challenge_id) DESC, s.hacker_id