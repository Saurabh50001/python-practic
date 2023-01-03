import pymysql as mq
# server connection  or database connection 
mysql1=mq.connect(
    host="localhost",
    user="root",
    passwd="",
    database="school"
)
mycursor=mysql1.cursor()
print("{:<20} {:<20} {:<20} {:<20}".format("student id","student name","student email","student class"))
try:
    # order & limit arange the data into accending or desending order
    # ASC represent accending order and DESC represent desending order
    # In limit 0 represent starting point and 2 represent how many data display
    
    # sql="select * from student order by st_id DESC LIMIT 0,2"

    # searching 
    name=input("Enter the student name:-")
    # for using like left and right both
    # sql="select * from student where st_name like'%"+name+"%'"
    sql="select * from student where st_name='"+name+"'"
    mycursor.execute(sql)
    sdata=mycursor.fetchall()

    for s in sdata:
        print("{:<20} {:<20} {:<20} {:<20}".format(s[0],s[1],s[2],s[3]))
except:
    print("Error..")