 WITH final AS (
    SELECT 
      DATE_PART('year', transaction_date) AS "year",
      product_id,
      SUM(spend) AS curr_year_spend,
      LAG(SUM(spend)) OVER(PARTITION BY product_id ORDER BY DATE_PART('year', transaction_date)) AS prev_year_spend 
    FROM user_transactions
    GROUP BY DATE_PART('year', transaction_date), product_id
          )
          
          
SELECT
  *,
  ROUND(100.0*(curr_year_spend - prev_year_spend)/prev_year_spend,2) AS yoy_rate
FROM final
