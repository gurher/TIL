WITH table1 AS 
        (
        SELECT 
            user_id,
            spend,
            transaction_date,
            DENSE_RANK() OVER(PARTITION BY user_id ORDER BY transaction_date ASC) AS ranking
            
        FROM transactions
        ORDER BY 1,3 DESC
            )
  
SELECT 
    user_id,
    spend,
    transaction_date
FROM table1
WHERE ranking = 3