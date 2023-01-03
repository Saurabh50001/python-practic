
import sqlite3
conn=sqlite3.connect("sqlite.db")
# set the limit 
# 2 represent how many data show
# 0 represent where to start
# data=conn.execute("SELECT * FROM student limit 0,2")
data=conn.execute("SELECT * FROM student")
print("STUDENT ID","STUDENT NAME","STUDENT CLASS", "STUDENT EMAIL")
for n in data:
    print(n[0],"    ",n[1],"      ",n[2],"            ",n[3])  
    # it data is in tupple format and it iratete with index no 
data=conn.execute("SELECT * FROM fee")
print("fee sl","STUDENT NAME","Amount")
for n in data:
    print(n[0],"    ",n[1],"      ",n[2]) 
print()
print()

# searching query
st_name=input("enter the student name:-")
st_class=input("Enter the student class:-")
# select * from student where st_name =st_name='"+st_name+"'
# "=" is use to search for where writen full name 
# "like" is use to search for where writen only one letter of the selected name
# there is also use "or" and "and" for searching 
data=conn.execute("SELECT * FROM student where st_name like '%"+st_name+"%' and st_class='"+st_class+"'  ")
for n in data:
    print(n[0],"    ", n[1],"    ", n[2],"     ",n[3])   