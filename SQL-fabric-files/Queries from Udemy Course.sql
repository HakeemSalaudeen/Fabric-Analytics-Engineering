SELECT count(*)  FROM departments;

SELECT order_status, count(*) AS order_count
FROM orders 
GROUP BY 1
ORDER BY 2 DESC;

SELECT  count(order_status) AS order_count
FROM orders 
ORDER BY 1 DESC;

SELECT order_item_order_id, sum (order_item_order_id) AS revenue
FROM order_items 
GROUP BY 1
ORDER BY 2 DESC;

SELECT order_item_order_id, sum (order_item_subtotal) AS revenue
FROM order_items 
GROUP BY 1
ORDER BY 2 DESC;

SELECT order_date, count(*) AS order_count
FROM orders 
WHERE order_status IN ('COMPLETE', 'CLOSED')
GROUP BY 1
	HAVING count (*) >= 120
ORDER BY 2 DESC;


-- Inner join
SELECT o.*,
	oi.order_item_product_id,
	oi.order_item_subtotal
FROM orders   o
	JOIN order_items  oi 
	ON o.order_id = oi.order_item_order_id


-- To create views 

CREATE VIEW order_details_v
AS
SELECT o.*,
	oi.order_item_product_id,
	oi.order_item_subtotal
FROM orders   o
	JOIN order_items  oi 
	ON o.order_id = oi.order_item_order_id

-- Testing the view 
SELECT *
FROM order_details_v

-- 	To modifythe view 
CREATE OR REPLACE VIEW order_details_v
AS
SELECT o.*,
	oi.order_item_product_id,
	oi.order_item_subtotal,
	oi.order_item_id
FROM orders   o
	JOIN order_items  oi 
	ON o.order_id = oi.order_item_order_id
	
-- Testing the modified view 
SELECT *
FROM order_details_v


-- Revenue per day 

SELECT o.order_date,
	oi.order_item_product_id,
	round (sum (oi.order_item_subtotal) ::numeric, 2) AS order_revenue,
	oi.order_item_id
FROM orders   o
	JOIN order_items  oi 
		ON o.order_id = oi.order_item_order_id
WHERE o.order_status IN ('COMPLETE', 'CLOSED')
GROUP BY 1, 2, 4
ORDER BY 1, 3 DESC;


-- CTA's CREATE TABLE AS SELECT
-- Create a Table related to order count by status 

-- Order count by status 
SELECT order_status, count(*) AS order_count
FROM orders 
GROUP BY 1;

-- Creating a table with the order status 
CREATE TABLE order_count_by_status
AS
SELECT order_status, count(*) AS order_count
FROM orders 
GROUP BY 1;

-- Testing the table we created 
SELECT *
FROM order_count_by_status