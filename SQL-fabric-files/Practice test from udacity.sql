select * from orders limit 10

-- occurred_at, account_id,channel columns of the web_events table, and limits the output to only the first 15 rows.
	
select occurred_at, account_id, channel
from web_events
limit 15;

-- order by 
select  id, occurred_at, total_amt_usd
from orders 
order by occurred_at 
limit 10

select id, account_id, total_amt_usd
from orders 
order by total_amt_usd desc
limit 5


select id, account_id, total_amt_usd
from orders 
order by total_amt_usd 
limit 20

-- order by 2
select id, account_id, total_amt_usd
from orders 
order by account_id, total_amt_usd desc

select id, account_id, total_amt_usd
from orders 
order by total_amt_usd desc, account_id 

-- where clause 
select *
from orders 
where gloss_amt_usd >= 1000 
order by gloss_amt_usd desc
limit 5

select *
from orders 
where total_amt_usd < 500 
limit 5

select name, website, primary_poc
from accounts
where name = 'Exxon Mobil'

select name, website, primary_poc
from accounts
where name <> 'Exxon Mobil'

select name, website, primary_poc
from accounts
where name != 'Exxon Mobil'
	
-- Arithmetic operators 
select (standard_amt_usd/standard_qty) as unit_price, id, account_id
from orders 
limit 5

SELECT id, account_id, 
       (poster_amt_usd/(standard_amt_usd + gloss_amt_usd + poster_amt_usd))*100 AS post_per
FROM orders
LIMIT 10;

-- LIKE
select *
from accounts
where name like 'c%'

select *
from accounts
where name like '%one%'

select *
from accounts
where name like '%s'

-- IN 
select name, primary_poc, sales_rep_id
from accounts
where name IN ('Walmart','Target', 'Nordstrom');

select account_id, channel
from web_events
where channel IN ('organic', 'adwords');

-- NOT IN 
select name, primary_poc, sales_rep_id
from accounts
where name NOT IN ('Walmart','Target', 'Nordstrom');

select account_id, channel
from web_events
where channel NOT IN ('organic', 'adwords');

select name
from accounts 
where name NOT like ('C%')

select name
from accounts 
where name NOT like ('%one%')

select name
from accounts 
where name NOT like ('%s')

-- AND and BETWEEN operators
select *
from orders
where standard_qty > 1000 and poster_qty = 0 and gloss_qty = 0

select *
from accounts
where name not like 'C%' AND name like '%s'

select occurred_at, gloss_qty
from orders 
where gloss_qty between 24 and 29; 

select *
from web_events
where channel IN ('organic', 'adwords') and occurred_at > '2015-12-31' and occurred_at < '2017-01-01'
order by occurred_at desc

select *
from web_events
where channel IN ('organic', 'adwords') and occurred_at between '2016-01-01' and '2017-01-01'
order by occurred_at desc

-- OR operator 
select id 
from orders 
where gloss_qty > 4000 or poster_qty > 4000

select *
from orders 
where (standard_qty = 0) 
		and (gloss_qty > 1000 or poster_qty > 1000)


select *
from accounts
where (name like 'C%' OR name like 'W%')
		AND (primary_poc like '%ana%' or primary_poc like '%Ana%')
		And (primary_poc not like '%eana%')
		

select *
from accounts
where (name like 'C%' OR name like 'W%')
		AND ((primary_poc like '%ana%' or primary_poc like '%Ana%')  
		And primary_poc not like '%eana%');




























