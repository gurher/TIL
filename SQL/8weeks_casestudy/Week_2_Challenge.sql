
-- A. Pizza Metrics

-- 1) How many pizzas were ordered?

SELECT 
	COUNT(customer_orders.order_id),
    COUNT(customer_orders.pizza_id)
FROM pizza_runner.customer_orders customer_orders


-- 2) How many unique customer orders were made?

SELECT 
	COUNT(DISTINCT (customer_orders.customer_id,customer_orders.pizza_id))
FROM pizza_runner.customer_orders customer_orders


-- 3) How many successful orders were delivered by each runner?


SELECT COUNT(DISTINCT runner_orders.order_id)
FROM pizza_runner.runner_orders runner_orders 
WHERE runner_orders.pickup_time != 'null'

-- 4) How many of each type of pizza was delivered?

SELECT 
	customer_orders.pizza_id,
    COUNT(*)
FROM (
  SELECT runner_orders.order_id
  FROM pizza_runner.runner_orders runner_orders 
  WHERE runner_orders.pickup_time != 'null'
	) delivered_orders
INNER JOIN pizza_runner.customer_orders customer_orders    
	ON delivered_orders.order_id = customer_orders.order_id
GROUP BY 1
ORDER BY 1



-- 5) How many Vegetarian and Meatlovers were ordered by each customer?

SELECT 
	customer_orders.customer_id,
    pizza_names.pizza_name, 
    COUNT(*)
FROM (
  SELECT runner_orders.order_id	
  FROM pizza_runner.runner_orders runner_orders 
  WHERE runner_orders.pickup_time != 'null'
	) delivered_orders
INNER JOIN pizza_runner.customer_orders customer_orders    
	ON delivered_orders.order_id = customer_orders.order_id
LEFT JOIN pizza_runner.pizza_names pizza_names
	ON customer_orders.pizza_id = pizza_names.pizza_id
GROUP BY 1,2
ORDER BY 1


-- 6) What was the maximum number of pizzas delivered in a single order?

WITH final AS (
SELECT 
	customer_orders.order_id,
    COUNT(*),
    ROW_NUMBER() OVER(ORDER BY COUNT(*) DESC)    
FROM (
  SELECT runner_orders.order_id
  FROM pizza_runner.runner_orders runner_orders 
  WHERE runner_orders.pickup_time != 'null'
	) delivered_orders
INNER JOIN pizza_runner.customer_orders customer_orders    
	ON delivered_orders.order_id = customer_orders.order_id
GROUP BY 1
  )
  
SELECT order_id
FROM final
WHERE row_number = 1



-- 7) For each customer, how many delivered pizzas had at least 1 change and how many had no changes?
SELECT 
	customer_id,
    SUM(CASE WHEN new_table.exclusions IS NOT NULL OR new_table.extras IS NOT NULL THEN 1 ELSE 0 END ) , 
    SUM(CASE WHEN new_table.exclusions IS NULL AND new_table.extras IS NULL THEN 1 ELSE 0 END) 

FROM (SELECT 
          customer_orders.order_id,
          customer_orders.customer_id,
          customer_orders.pizza_id, 
          CASE WHEN customer_orders.exclusions IS NULL OR customer_orders.exclusions = 'null' OR customer_orders.exclusions = ''
          THEN NULL ELSE customer_orders.exclusions END,
          CASE WHEN customer_orders.extras IS NULL OR customer_orders.extras = 'null' OR customer_orders.extras = '' THEN NULL ELSE customer_orders.extras END,
          customer_orders.order_time
          FROM pizza_runner.customer_orders customer_orders   
          INNER JOIN pizza_runner.runner_orders delivered_orders 
          ON delivered_orders.order_id = customer_orders.order_id
          WHERE delivered_orders.pickup_time != 'null'
         ) new_table
GROUP BY 1      
ORDER BY 1 ASC


-- 8) How many pizzas were delivered that had both exclusions and extras?

WITH final AS (

    SELECT 
        CASE WHEN new_table.exclusions IS NOT NULL AND new_table.extras IS NOT NULL THEN 'both' ELSE 'else' END AS topping_changes
    FROM (SELECT 
            customer_orders.order_id,
            customer_orders.customer_id,
            customer_orders.pizza_id, 
            CASE WHEN customer_orders.exclusions IS NULL OR customer_orders.exclusions = 'null' OR customer_orders.exclusions = ''
            THEN NULL ELSE customer_orders.exclusions END,
            CASE WHEN customer_orders.extras IS NULL OR customer_orders.extras = 'null' OR customer_orders.extras = '' THEN NULL ELSE customer_orders.extras END,
            customer_orders.order_time
          FROM pizza_runner.customer_orders customer_orders   
          INNER JOIN pizza_runner.runner_orders delivered_orders 
              ON delivered_orders.order_id = customer_orders.order_id
          WHERE delivered_orders.pickup_time != 'null'
          ) new_table
	)

SELECT COUNT(*)
FROM final
WHERE final.topping_changes = 'both'


-- 9) What was the total volume of pizzas ordered for each hour of the day?

WITH final AS (
    SELECT 
  		new_table.order_id,
		EXTRACT(HOUR FROM DATE_TRUNC('hour', new_table.order_time)) AS hour
    FROM (SELECT 
            customer_orders.order_id,
            customer_orders.customer_id,
            customer_orders.pizza_id, 
            CASE WHEN customer_orders.exclusions IS NULL OR customer_orders.exclusions = 'null' OR customer_orders.exclusions = ''
            THEN NULL ELSE customer_orders.exclusions END,
            CASE WHEN customer_orders.extras IS NULL OR customer_orders.extras = 'null' OR customer_orders.extras = '' THEN NULL ELSE customer_orders.extras END,
            customer_orders.order_time
          FROM pizza_runner.customer_orders customer_orders   
          INNER JOIN pizza_runner.runner_orders delivered_orders 
              ON delivered_orders.order_id = customer_orders.order_id
          WHERE delivered_orders.pickup_time != 'null'
          ) new_table
  		)

SELECT
		final.hour
		, COUNT(DISTINCT final.order_id)
FROM final
GROUP BY 1
ORDER BY 1

-- 10) What was the volume of orders for each day of the week?

WITH final AS (
    SELECT 
  		new_table.order_id,
        new_table.order_time,
		-- EXTRACT(DAY FROM DATE_TRUNC('day', new_table.order_time)) AS day,
        TO_CHAR(new_table.order_time, 'DAY') AS day
    FROM (SELECT 
            customer_orders.order_id,
            customer_orders.customer_id,
            customer_orders.pizza_id, 
            CASE WHEN customer_orders.exclusions IS NULL OR customer_orders.exclusions = 'null' OR customer_orders.exclusions = ''
            THEN NULL ELSE customer_orders.exclusions END,
            CASE WHEN customer_orders.extras IS NULL OR customer_orders.extras = 'null' OR customer_orders.extras = '' THEN NULL ELSE customer_orders.extras END,
            customer_orders.order_time
          FROM pizza_runner.customer_orders customer_orders   
          INNER JOIN pizza_runner.runner_orders delivered_orders 
              ON delivered_orders.order_id = customer_orders.order_id
          WHERE delivered_orders.pickup_time != 'null'
          ) new_table
  		)

SELECT
		final.day
		, COUNT(DISTINCT final.order_id)
FROM final
GROUP BY 1
ORDER BY 1




-- B. Runner and Customer Experience

    
-- 1) How many runners signed up for each 1 week period? (i.e. week starts 2021-01-01)


SELECT 
	DATE_TRUNC('week', runners.registration_date),
    COUNT(DISTINCT runners.runner_id)
FROM pizza_runner.runners runners
GROUP BY 1
ORDER BY 1 ASC



-- 2) What was the average time in minutes it took for each runner to arrive at the Pizza Runner HQ to pickup the order?

SELECT 
	runner_orders.runner_id,
	AVG(CAST(SUBSTRING(runner_orders.duration ,1,2) AS INT))
FROM pizza_runner.runner_orders runner_orders
WHERE runner_orders.pickup_time != 'null'
GROUP BY 1
ORDER BY 1 ASC

-- 3) Is there any relationship between the number of pizzas and how long the order takes to prepare?



WITH order_counts AS (
	SELECT
        customer_orders.order_id,
        COUNT( customer_orders.pizza_id) AS counts
    FROM pizza_runner.customer_orders customer_orders
    GROUP BY 1
    ORDER BY 1
  				)
                
SELECT
	-- order_counts.order_id,        
    order_counts.counts,
	AVG(CAST(SUBSTRING(runner_orders.duration ,1,2) AS INT))

FROM order_counts
INNER JOIN pizza_runner.runner_orders runner_orders
	ON runner_orders.order_id = order_counts.order_id
WHERE runner_orders.pickup_time != 'null'    
GROUP BY counts

-- WITH table1 AS (

--     SELECT 
--         customer_orders.order_id,
--         customer_orders.customer_id,
--         customer_orders.pizza_id,
--         CASE WHEN customer_orders.exclusions IS NULL OR customer_orders.exclusions = 'null' OR customer_orders.exclusions = '' THEN FALSE ELSE TRUE END AS exclusions, 
--         CASE WHEN customer_orders.extras IS NULL OR customer_orders.extras = 'null' OR customer_orders.extras = '' THEN FALSE ELSE TRUE END AS extras,
--         CAST(SUBSTRING(runner_orders.duration ,1,2) AS INT) AS duration

--     FROM pizza_runner.customer_orders customer_orders 
--     INNER JOIN pizza_runner.runner_orders runner_orders
--         ON runner_orders.order_id = customer_orders.order_id
--     WHERE runner_orders.pickup_time != 'null'    

--   				)
                
-- SELECT 

-- 	table1.exclusions,
--     AVG(table1.duration)
	
-- FROM table1
-- GROUP BY 1


-- 4) What was the average distance travelled for each customer?

-- SELECT 
-- 		DISTINCT 
-- 		customer_orders.order_id,
--         customer_orders.customer_id,
--         SUBSTRING(runner_orders.distance,1,4),
--         -- POSITION(runner_orders.distance,),
        
--         -- INSTR(runner_orders.distance,' '),
        
--         -- regexp_substr(runner_orders.distance, '^\d+'),
--         runner_orders.distance

-- FROM pizza_runner.customer_orders customer_orders 
-- INNER JOIN pizza_runner.runner_orders runner_orders
-- 	ON runner_orders.order_id = customer_orders.order_id
-- WHERE runner_orders.pickup_time != 'null' 



-- 5) What was the difference between the longest and shortest delivery times for all orders?
-- 6) What was the average speed for each runner for each delivery and do you notice any trend for these values?
-- 7) What is the successful delivery percentage for each runner?
