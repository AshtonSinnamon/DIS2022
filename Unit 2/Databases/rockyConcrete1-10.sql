/* SQL1 */
select cust_name
from customers;
/* SQL2 */
select description, list_price
from products;
/* SQL3 */
select *
from customers;
/* SQL4 */
select *
from products
where list_price > 100;
/* SQL5 */
select *
from customers 
where curr_bal > 250;
/* SQL6 */
select prod_group
from products
where prod_group is 'A';
/* SQL7 */
select order_price
from order_details
where order_price > 1000;
/* SQL8 */
select cust_no, cust_name as Name, cr_limit, curr_bal * 0.9 as 'discounted price'
from customers
where curr_bal > cr_limit;
/* SQL9 */
select post_code
from customers
where post_code between 4000 and 4999;
/* SQL10 */
select prod_code, qty_on_hand, remake_level, remake_qty
from products
where qty_on_hand < remake_level;