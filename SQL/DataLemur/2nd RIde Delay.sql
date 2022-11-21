

WITH moment_user AS (
    SELECT 
    r.ride_id,
    r.user_id,
    u.registration_date,
    r.ride_date,
    ROW_NUMBER() OVER(PARTITION BY r.user_id ORDER BY r.ride_date) AS rnk,
    r.ride_date - u.registration_date AS date_diff,
    CASE WHEN u.registration_date = r.ride_date THEN 'moment_user' ELSE 'others' END AS user_group   
    FROM users u
    INNER JOIN rides r
      ON u.user_id = r.user_id
    
        )
        
        
SELECT
  ROUND(AVG(date_diff),2) AS average_delay
  
FROM moment_user
WHERE user_id IN (SELECT DISTINCT user_id
                  FROM moment_user
                  WHERE user_group = 'moment_user') 
    AND rnk = 2                
;

-- SOLUTION



-- WITH moment_users AS (
--   SELECT DISTINCT users.user_id
--   FROM users 
--   JOIN rides
--   ON users.user_id = rides.user_id
--     AND users.registration_date = rides.ride_date),

-- rides_cte AS (
-- SELECT 
--   rides.user_id,
--   rides.ride_date,
--   ROW_NUMBER() OVER (
--     PARTITION BY users.user_id ORDER BY rides.ride_date) AS ride_nr,
--   LAG(rides.ride_date) OVER (
--     PARTITION BY users.user_id ORDER BY rides.ride_date) AS lag_ride_date
-- FROM moment_users AS users
-- LEFT JOIN rides
--   ON users.user_id = rides.user_id
-- )    
    
    
    
-- SELECT ROUND(AVG(ride_date - lag_ride_date),2) AS average_delay
-- FROM rides_cte
-- WHERE ride_nr=2;



