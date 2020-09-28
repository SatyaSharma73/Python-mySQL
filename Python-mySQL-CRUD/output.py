import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='2964',database='python')

mycursor=mydb.cursor()
mycursor.execute("select * from py")
myresult=mycursor.fetchall()
for row in myresult:
    print(row)