import sqlite3

con = sqlite3.connect('../Databases/rockyconcrete.db')

con.row_factory = sqlite3.Row
cur = con.cursor()

run = True
while run:
    print("Enter the number from the following options:")
    print("1 - Get Customer Details")
    print("2 - Get Order Details")
    print("3 - Get Product Details")
    print("4 - Quit \n")
    choice = input("Make a Choice: ")
    if choice == "1":
        name = input("Name: ")
        sql = """
                select *
                from customers
                where cust_name like ?
                order by cust_name asc;"""
        cur.execute(sql, ("%" + name + "%",))
        results = cur.fetchall()
        for row in results:
            print(row['cust_no'], row['cust_name'], row['street'], row['town'], row['post_code'], row['cr_limit'],
                  row['curr_bal'])
        run = True

    elif choice == "2":
        od = input("Order Number: ")
        sql = """
                select *
                from order_details
                where order_no like ?
                order by order_no asc;"""
        cur.execute(sql, ("%" + od + "%",))
        results = cur.fetchall()
        for row in results:
            print(row['order_no'], row['prod_code'], row['order_qty'], row['order_price'])
        run = True

    elif choice == "3":
        name = input("Product Name: ")
        sql = """
                select *
                from products
                where prod_code like ?;"""
        cur.execute(sql, ("%" + name + "%",))
        results = cur.fetchall()
        for row in results:
            print(row['prod_code'], row['description'], row['prod_group'], row['list_price'], row['qty_on_hand'], row['remake_level'], row['remake_qty'])
        run = True

    elif choice == "4":
        print("Goodbye")
        quit()

    else:
        print("Error")
        run = True
