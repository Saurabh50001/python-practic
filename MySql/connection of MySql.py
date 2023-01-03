import pymysql as mq
# server Name -> localhost
# username-> root
# password -> " "
myobj=mq.connect(
    host="localhost",
    user="root",
    passwd="",
    database="school"
)
cursorobj=myobj.cursor()
try:
    print("saurabh")
    db="create database school"
    cursorobj.execute(db)
    print("database created")
except:
    print("database error..")
