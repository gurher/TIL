SELECT CONCAT(name,'(' ,SUBSTR(occupation,1,1),')')
FROM occupations
ORDER BY name;

SELECT CONCAT('There are a total of ' , X.num , ' ' , LOWER(X.occupation), 's.')
FROM
  (SELECT occupation,
          COUNT(DISTINCT name) AS num
   FROM occupations
   GROUP BY occupation) X
ORDER BY X.num,
         X.occupation;