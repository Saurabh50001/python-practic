import sqlite3
conn=sqlite3.connect("sqlite.db")
conn.execute('''
    create table fees(
        st_sl int auto_increment,
        st_name varchar(50),
        st_amount int(20)
       
    )
'''
)
print("Table created")

conn.close()