import sqlite3
conn=sqlite3.connect("sqlite.db")

ins='''
    insert into student(st_name, st_class,st_email) VALUES('Pankaj','12th','pankaj@gmail.com')
'''
ins1='''
    insert into teacher(t_name,t_email,t_phone)VALUES('Pinki','pinki43@gamil.com','878968687687')
'''
ins2='''
    insert into fees(st_name,st_amount)VALUES('Ravi','4000')
'''
conn.execute(ins)
conn.execute(ins1)
conn.execute(ins2)
print("Data inserted")

conn.commit() # it is use to do new data for ( insert, update, delete)
conn.close