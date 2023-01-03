import sqlite3
conn=sqlite3.connect("sqlite.db")
print("STUDENT SL","STUDENT NAME","AMOUNT")
# data=conn.execute("select * from fees as f inner join student as s on f.st_name= s.st_name")
data=conn.execute("select f.st_sl,f.st_name,f.st_amount from fees as f inner join student as s on f.st_name= s.st_name")
for a in data:
    print(a)
conn.close()