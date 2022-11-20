WITH table1 AS (
    SELECT 
        category,
        product,
        SUM(spend) AS total,
        DENSE_RANK() OVER ( PARTITION BY category ORDER BY SUM(spend) DESC) AS ranking
        
    FROM product_spend
    WHERE DATE_PART('year',transaction_date) = '2022'
    GROUP BY category, product
        )
        
SELECT 
    category,
    product,
    total
FROM table1
WHERE ranking < 3