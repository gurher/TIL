SELECT Start_Date, MIN(End_Date)
FROM
  (SELECT Start_Date
   FROM Projects
   WHERE Start_Date NOT IN
       (SELECT End_Date
        FROM Projects)) A,
  (SELECT End_Date
   FROM Projects
   WHERE End_Date NOT IN
       (SELECT Start_Date
        FROM Projects)) B
WHERE Start_Date < End_Date
GROUP BY Start_Date
ORDER BY (MIN(End_Date) - Start_Date), Start_Date;

-- SELECT

-- FROM (SELECT p.Start_Date AS start_date, p.End_Date AS end_date
--       FROM Projects p
--       WHERE NOT EXISTS (SELECT b.Start_Date 
--                         FROM Projects b
--                         WHERE b.End_Date = p.Start_Date) ) AS sd 

-- LEFT JOIN (SELECT p.Start_Date AS start_date, p.End_Date AS end_date
--            FROM Projects p
--            WHERE NOT EXISTS (SELECT b.Start_Date
--                         FROM Projects b
--                         WHERE b.Start_Date = p.End_Date) ) AS ed

-- ON sd.start_date < ed.end_date

