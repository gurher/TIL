SELECT 
    final_table.city,
    final_table.len
    
FROM (SELECT
            city_length.city,
            city_length.len,
            ROW_NUMBER() OVER(PARTITION BY city_length.len ORDER BY city_length.city ) AS 'row_number'
      FROM (   SELECT city, LENGTH(city) AS "len"
               FROM station
               WHERE LENGTH(city) = ( SELECT MAX(LENGTH(city))
                                       FROM station )
                   OR LENGTH(city) = ( SELECT MIN(LENGTH(city))
                                       FROM station ) 
               ORDER BY 2 ASC, 1 ASC ) AS city_length
      ) AS final_table
WHERE final_table.row_number = 1   




-- SELECT city, LENGTH(city) FROM station ORDER BY LENGTH(city), city LIMIT 1;
-- SELECT city, LENGTH(city) FROM station ORDER BY LENGTH(city) DESC, city LIMIT 1;