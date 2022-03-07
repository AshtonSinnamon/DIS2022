--Joint Queries
--JQ1
select od.prod_code, description, order_price, order_no, order_qty
from order_details od, products p
where od.prod_code = p.prod_code
and order_no = 1234;

select prod_code, description, order_price, order_no, order_qty
from order_details od
inner join products p
on od.prod_code = p.prod_code
and order_no = 1234;

-- JQ2
select cust_no, street, town, post_code, order_date
from customers c, orders o
where c.cust_no = o.cust_no
and order_date like '1706%'
order by order_date asc;

-- JQ3
select order_no, prod_code, order_price, list_price
from products p, order_details od
where p.prod_code = od.prod_code
and order_price <> list_price;
-- <> means dosent equal (!=), both work in SQL


--JQ4
select cust_name, order_date, order_price * order_qty as line_price
from customers c, orders o, order_details od
where c.cust_no = o.cust_no
and o.order_no = od.order_no
and line_price > 500
order by order_date asc,line_price desc;


--JQ5
select description, cust_name
from customers c, products p, order_details od, orders o
where c.cust_no = o.cust_no
and o.order_no = od.order_no
and od.prod_code = p.prod_code
and town = 'Brisbane';

--JQ6
select cust_name, curr_bal, cr_limit, order_date, order_price * order_qty as line_price
from customers c, order_details od, orders o
where c.cust_no = o.cust_no
and o.order_no = od.order_no
and cr_limit < curr_bal;

--JQ7
select cust_name
from customers c,  orders o, order_details od
where c.cust_no = o.cust_no
and o.order_no = o.order_no
and prod_code = 'GNOME'
and order_date like '1704%';

--JQ8
select prod_code, description, order_date, order_qty
from orders o, order_details od, products p
where o.order_no = od.order_no
and prod_code like "G";
--JQ9
select prod_code, order_no, order_date
from orders o, products p, order_details od
where o.order_no = od.order_no
and od.prod_code = p.prod_code
and order_qty < remake_qty;
--JQ10
select cust_name, order_qty, list_price, order_price
from customers c, order_details od, products p, orders o
where c.cust_no = o.cust_no
and o.order_no = od.order_no
and od.prod_code = p.prod_code
and prod_group = "A"
and post_code between 4000 and 4999;