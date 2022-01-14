


SELECT 
    IF(g.grade < 8, NULL, s.name) name
    , g.grade
    , s.marks
FROM students s 
LEFT JOIN grades g
    ON s.marks >= g.min_mark AND s.marks <= g.max_mark
ORDER BY g.grade DESC, s.name


