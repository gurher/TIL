
WITH src AS (
  SELECT 
  
    s.user_id,
    s.signup_date,
    u.product_id,
    u.purchase_amount,
    u.purchase_date,
    CASE WHEN u.purchase_date IS NULL OR u.purchase_date BETWEEN s.signup_date AND s.signup_date + INTERVAL '7' DAY THEN 'purchased_users' ELSE 'others' END user_status
    
  FROM signups s
  LEFT JOIN user_purchases u
    ON s.user_id = u.user_id 

      )

SELECT

ROUND(100.0 * COUNT( DISTINCT CASE WHEN product_id IS NOT NULL THEN user_id ELSE NULL END ) / COUNT(DISTINCT user_id),2) AS single_purchase_pct
FROM src
WHERE user_status = 'purchased_users'


-- SELECT ROUND(
--   100.0 * 
--     COUNT(DISTINCT purchases.user_id) / 
--     COUNT(DISTINCT signups.user_id), 2) AS same_week_purchases_pct
-- FROM signups
-- LEFT JOIN user_purchases AS purchases
--   ON signups.user_id = purchases.user_id
-- WHERE purchases.purchase_date IS NULL
--   OR (purchases.purchase_date BETWEEN signups.signup_date 
--   AND (signups.signup_date + '7 days'::INTERVAL));

