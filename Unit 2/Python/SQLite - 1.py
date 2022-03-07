import sqlite3

con = sqlite3.connect('../Databases/rockyconcrete.db')

con.row_factory = sqlite3.Row
cur = con.cursor()

# sql = """
#         select *
#         from customers
#         where town = 'Brisbane';"""
#
# cur.execute(sql)
# results = cur.fetchall()
#
# print(results)

# parameter query
town = input("Town to search for: ")
credit = int(input("Credit Limit: "))

sql = """
        select *
        from customers
        where town like ?
        and cr_limit >= ?;"""

cur.execute(sql, ('%'+town+'%', credit,))
results = cur.fetchall()

if len(results) > 0:
    for row in results:
        if credit >= 3000:
            print(row['cust_name'], 'has a credit limit of', row['cr_limit'], 'lives in', row['street'], 'in', row['town'])
else:
    print('No records found')