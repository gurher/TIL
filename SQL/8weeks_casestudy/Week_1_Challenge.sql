

/* --------------------
   Case Study Questions
   --------------------*/

-- 1. What is the total amount each customer spent at the restaurant?

SELECT
  	sales.customer_id,
    SUM(menu.price)
FROM dannys_diner.sales sales
INNER JOIN dannys_diner.menu menu
	ON sales.product_id = menu.product_id
GROUP BY sales.customer_id
ORDER BY 1


-- 2. How many days has each customer visited the restaurant?

SELECT 
	sales.customer_id,
    COUNT(DISTINCT sales.order_date)
FROM dannys_diner.sales sales
GROUP BY 1
ORDER BY 1





-- 3. What was the first item from the menu purchased by each customer?

-- SELECT
-- 	sales.customer_id,
--     DATE_TRUNC('day',sales.order_date) AS "day",
--     menu.product_name,
--     ROW_NUMBER(sales.order_date) OVER(PARTITION BY sales.customer_id ORDER BY sales.customer_id) AS "min" 
   
-- FROM dannys_diner.sales sales
-- LEFT JOIN dannys_diner.menu menu
-- 	ON sales.product_id = menu.product_id
    
    
SELECT
	DISTINCT
	first_date.customer_id,
	first_date.date,
	menu.product_name
    
FROM (SELECT
          sales.customer_id,
          MIN(sales.order_date) AS "date"
      FROM dannys_diner.sales sales
      GROUP BY 1) first_date
INNER JOIN dannys_diner.sales sales
	ON first_date.customer_id = sales.customer_id
    AND first_date.date = sales.order_date    
INNER JOIN dannys_diner.menu menu
	ON sales.product_id = menu.product_id
ORDER BY 1       
      
    



-- 4. What is the most purchased item on the menu and how many times was it purchased by all customers?

SELECT 
	menu.product_name,
    product_count.count

FROM (SELECT 
          sales.product_id,
          COUNT(sales.product_id)
      FROM dannys_diner.sales sales
      GROUP BY 1
      ORDER BY 1 ASC) product_count
INNER JOIN dannys_diner.menu menu
	ON product_count.product_id = menu.product_id


-- 5. Which item was the most popular for each customer?

SELECT
	 sales.customer_id, 
     menu.product_name,
     COUNT(*)
FROM dannys_diner.sales sales
INNER JOIN dannys_diner.menu  menu
	ON sales.product_id = menu.product_id
GROUP BY sales.customer_id, menu.product_name    
ORDER BY 1 ASC, 3 DESC    
    

-- 6. Which item was purchased first by the customer after they became a member?

WITH final_table AS (
SELECT 
	after_join.customer_id,
    after_join.order_date,
    menu.product_name,
    ROW_NUMBER() OVER(PARTITION BY after_join.customer_id ORDER BY after_join.order_date ASC)
    
FROM ( SELECT 	
           sales.customer_id,
           sales.order_date,
           sales.product_id
       FROM dannys_diner.sales sales
       INNER JOIN dannys_diner.members members
           ON sales.customer_id = members.customer_id
       WHERE sales.order_date >= members.join_date ) AS after_join
INNER JOIN dannys_diner.menu menu
	ON after_join.product_id = menu.product_id
)

SELECT
	customer_id,
	product_name
FROM final_table
WHERE row_number = 1





-- 7. Which item was purchased just before the customer became a member?

WITH final_table AS (
  SELECT 
      sales.customer_id,
      sales.order_date,
      sales.product_id,
  	  menu.product_name,
      COALESCE(members.join_date , sales.order_date + INTERVAL '1' DAY) AS joined_date
  FROM dannys_diner.sales sales
  LEFT JOIN dannys_diner.members members
       ON sales.customer_id = members.customer_id
  INNER JOIN dannys_diner.menu menu
		  ON sales.product_id = menu.product_id
	),
    
final AS (    
SELECT 
	final_table.customer_id,
    final_table.product_name,
    ROW_NUMBER() OVER( PARTITION BY final_table.customer_id ORDER BY final_table.order_date)  
FROM final_table
WHERE order_date < joined_date 
	)
    
SELECT *
FROM final
WHERE row_number = 1

-- 8. What is the total items and amount spent for each member before they became a member?


SELECT 
	sales.customer_id,
    COUNT(menu.product_name),
    SUM(menu.price)
FROM dannys_diner.sales sales
INNER JOIN dannys_diner.members members
	ON sales.customer_id = members.customer_id
INNER JOIN dannys_diner.menu menu
	ON sales.product_id = menu.product_id
WHERE sales.order_date < members.join_date
GROUP BY 1
	


-- 9.  If each $1 spent equates to 10 points and sushi has a 2x points multiplier - how many points would each customer have?

WITH final AS (
  SELECT 
      sales.customer_id,
      menu.product_name,
      menu.price,
      CASE WHEN menu.product_name = 'sushi' THEN menu.price*20
      ELSE menu.price*10 END AS points    
  FROM dannys_diner.sales sales
  INNER JOIN dannys_diner.menu menu
      ON sales.product_id = menu.product_id
				)

SELECT 
	final.customer_id,
    SUM(points)
FROM final
GROUP BY 1



-- 10. In the first week after a customer joins the program (including their join date) they earn 2x points on all items, not just sushi - how many points do customer A and B have at the end of January?


SELECT
	final_table.customer_id,
    SUM(final_table.points)
	
FROM (SELECT 	
          sales.customer_id,
          menu.product_name,
          CASE WHEN sales.order_date >= members.join_date THEN menu.price*20 ELSE 0 END AS points
          -- IF(sales.order_date >= members.join_date,menu.price*2,0)		 
      FROM dannys_diner.sales sales
      INNER JOIN dannys_diner.members members
          ON sales.customer_id = members.customer_id
      INNER JOIN dannys_diner.menu menu
          ON sales.product_id = menu.product_id) final_table
GROUP BY 1


