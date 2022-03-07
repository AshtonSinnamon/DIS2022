from flask import Flask, render_template, url_for, request, redirect
import sqlite3

import os

app = Flask(__name__)

# connect to the database
con = sqlite3.connect("rockyconcrete.db", check_same_thread=False)
con.row_factory = sqlite3.Row

# create a cursor/pointer to navigate the database
cur = con.cursor()


@app.route('/')
@app.route('/index')
def index():
    sql = """
            select *
            from customers
            order by cust_name asc;"""
    cur.execute(sql)
    results = cur.fetchall()

    return render_template("index.html", customers=results, title="Customers List")


@app.route('/customer_details', methods=['GET'])
def customers_details():
    if request.args.get('cid'):
        id = int(request.args.get('cid'))
        sql = """select *
                from customers
                where cust_no = ?;"""

        cur.execute(sql, (id,))
        cust_results = cur.fetchone()

        sql = """
                select count(distinct o.order_no) as 'Order Count', max(order_date) as 'Last Order', sum(order_qty * order_price) as 'total price'
                from orders o, order_details od
                where o.order_no = od.order_no
                and cust_no = ?;"""

        cur.execute(sql, (id,))
        order_count = cur.fetchone()

        sql = """
                select order_date, order_no
                from orders
                where cust_no = ?
                order by order_date desc;"""

        cur.execute(sql, (id,))
        order_history = cur.fetchall()
        # for row in order_history:
        #     print(row['order_date'], row['order_no'])
        return render_template("customer_details.html", cdetails=cust_results, title="Customer Details",
                               ocount=order_count, order_history=order_history)

    else:
        return redirect(url_for("index"))


@app.route('/order_details')
def order_details():
    if request.args.get('oid'):
        oid = int(request.args.get('oid'))
        sql = """
                select *, order_qty * order_price as 'total'
                from order_details od, products p, orders o
                where od.prod_code = p.prod_code
                and o.order_no = od.order_no
                and od.order_no = ?;"""

        # p.prod_code, order_date, od.order_no, order_no, order_qty, order_price
        cur.execute(sql, (oid,))
        od_results = cur.fetchall()

        sql = """
                select sum(order_qty*order_price) as total
                from order_details
                where order_no = ?"""

        cur.execute(sql, (oid,))
        total = cur.fetchone()

        return render_template("order_details.html", od_results=od_results, title="Order Details", \
                               order_total=total)
    else:
        return redirect(url_for("index"))


@app.route('/product_details')
def products():
    if request.args.get('pid'):
        pid = (request.args.get('pid'))

        sql = """
                select *
                from products
                where prod_code = ?;"""

        cur.execute(sql, (pid,))
        product = cur.fetchone()

        return render_template('product_details.html', title="Product Details", proucts=product)
    else:
        return redirect(url_for("index"))


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 8080
    app.run(host, port, debug=True)
