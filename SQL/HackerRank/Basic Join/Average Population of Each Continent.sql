
SELECT country.Continent,
        FLOOR(AVG(city.population)) AS population
FROM country
LEFT JOIN city
    ON country.Code = city.CountryCode
GROUP BY country.Continent
HAVING AVG(city.population) IS NOT NULL
