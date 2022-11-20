SELECT 
  ROUND(CAST(SUM(CASE WHEN texts.signup_action = 'Confirmed' THEN 1 ELSE NULL END) AS DECIMAL) / COUNT(user_id),2) 
FROM emails
INNER JOIN texts
  ON emails.email_id = texts.email_id ;