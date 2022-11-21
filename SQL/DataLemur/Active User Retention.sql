WITH src AS (

  SELECT 
  
    ROW_NUMBER() OVER(PARTITION BY user_id ORDER BY event_date) as rwn,
    user_id,
    event_type,
    event_date,
    LAG(event_date) OVER(PARTITION BY user_id ORDER BY event_date) AS prv_date
    
  FROM user_actions
  WHERE event_type IN ('sign-in', 'like', 'comment')
  
    ),
  
final AS (  
  SELECT
    *,
    CASE WHEN DATE_PART('month', event_date) - DATE_PART('month', prv_date) = 1 THEN 'active' ELSE NULL END AS user_status,
    DATE_PART('month', event_date) AS months
  FROM src
  )
  
SELECT 
      months,
      COUNT(DISTINCT user_id)
FROM final
WHERE user_status = 'active'
  AND months = 7
GROUP BY 1

