-- Schema SQL Query SQL ResultsEdit on DB Fiddle
-- Example Query:
-- SELECT
-- 	runners.runner_id,
--     runners.registration_date,
-- 	COUNT(DISTINCT runner_orders.order_id) AS orders
-- FROM pizza_runner.runners
-- INNER JOIN pizza_runner.runner_orders
-- 	ON runners.runner_id = runner_orders.runner_id
-- WHERE runner_orders.cancellation IS NOT NULL
-- GROUP BY
-- 	runners.runner_id,
--     runners.registration_date;
    
    
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
WITH final AS (

    SELECT 
        CASE WHEN new_table.exclusions IS NOT NULL OR new_table.extras IS NOT NULL THEN 'change' ELSE 'No Change' END AS topping_changes

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
	final.topping_changes,
    COUNT(*)
FROM final
GROUP BY 1


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
