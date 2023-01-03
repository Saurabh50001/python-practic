import pymysql as mq
conn=mq.connect(
    host="localhost",
    user="root",
    passwd="",
    database="school"
)
mycursor=conn.cursor()
try:
    ins="INSERT INTO student (st_name,st_class,st_email) values(%s,%s,%s,)"
    t=[('raj','10th','raj@gmail.com'),('testing','10th','testing@gmail.com')]
    mycursor.executemany(ins,t)
    conn.commit()
    print("Insert Data")
except:
    print("Error..")