
SELECT 
    DISTINCT city.name
FROM city
LEFT JOIN country
    ON city.countrycode = country.code
WHERE country.continent = 'Africa'
