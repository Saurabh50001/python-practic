import pymysql as mq
conn=mq.connect(
    host="localhost",
    user="root",
    passwd="",
    database="school"
)
mysqlc=conn.cursor()
tc= "create table student(st_id INT primary key auto_increment, st_name varchar(50),st_class varchar(10), st_email varchar(50))"
mysqlc.execute(tc)