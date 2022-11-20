SELECT 

  age_breakdown.age_bucket,
  ROUND(100.0 * SUM( CASE WHEN activities.activity_type = 'send' THEN time_spent ELSE NULL END ) / SUM( CASE WHEN activities.activity_type IN ('open','send') THEN time_spent ELSE NULL END ),2) AS send,
  ROUND(100.0 * SUM( CASE WHEN activities.activity_type = 'open' THEN time_spent ELSE NULL END ) / SUM( CASE WHEN activities.activity_type IN ('open','send') THEN time_spent ELSE NULL END ),2) AS open
  
FROM activities
INNER JOIN age_breakdown
  ON activities.user_id = age_breakdown.user_id
GROUP BY age_breakdown.age_bucket ;