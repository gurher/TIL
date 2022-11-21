WITH final AS (
    SELECT 
      transaction_id,
      merchant_id,
      credit_card_id,
      amount,
      transaction_timestamp,
      EXTRACT(EPOCH FROM transaction_timestamp - LAG(transaction_timestamp) OVER(PARTITION BY merchant_id,credit_card_id, amount ORDER BY credit_card_id, transaction_timestamp))/60 minute_difference
      
    FROM transactions
          )

SELECT  COUNT(*)
FROM final
WHERE minute_difference < 11