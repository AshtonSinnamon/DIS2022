import sqlite3

# connect to the database
con = sqlite3.connect("people1.db")
con.row_factory = sqlite3.Row

# create a cursor/pointer to navigate the database
cur = con.cursor()

name = input("Name: ")
age = int(input("Age: "))
sex = input("Gender(M|F): ").upper()
earns = int(input("Earns: "))
likes = input("Likes: ")
dislikes = input("Dislikes: ")

while sex != "M" or "F":
    print("Gender must be M or F")
    sex = input("Gender(M|F): ").upper()

sql = """
        insert
        into members
        values(?,?,?,?,?,?)"""

try:
    cur.execute(sql, (name, age, sex, earns, likes, dislikes))
    con.commit()
    print("Data in database")
except:
    print("Error")