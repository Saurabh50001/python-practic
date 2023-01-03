import pymysql as mq
mysql=mq.Connect("localhost","root","","school")
cursorobj=mysql.cursor()
st_id=input("Enter the student id")
sql="DELETE from student where st_id=%s"
try:
    cursorobj.execute(sql,st_id)
    mysql.commit()
    print("student Deleted")
except:
    print("Error..")