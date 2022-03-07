# write the code:
# ask the user to enter the name of a customers, print out on the screen, their name, customer
# number and available credit
# Print also there most recent order number and date

import sqlite3

con = sqlite3.connect('../Databases/rockyconcrete.db')

con.row_factory = sqlite3.Row
cur = con.cursor()

name = input("Name: ")

sql = """
        select cust_name, cust_no, cr_limit - curr_bal as 'available'
        from customers
        where cust_name like ?;"""


cur.execute(sql, ('%'+name+'%',))
results = cur.fetchall()
# print(results)

for row in results:
    cust_no = row['cust_no']
    sql = """
                select max(order_no) as 'order_no', max(order_date) as 'order_date', cust_no
                from orders
                where cust_no = ?
                and order_no  ;"""

    cur.execute(sql,(cust_no,))
    result = cur.fetchall()

    if len(result) > 0:
        for line in result:
            print('Customer Number is:', row['cust_no'],)

                  #'Order Number,', row['max(order_no)'], 'Order date', row['max(order_date)'], '\n')