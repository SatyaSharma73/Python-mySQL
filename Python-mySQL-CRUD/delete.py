import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='2964',database='satyadb')

mycursor=mydb.cursor()
sql="DROP from employee Where name='aniket'"
mycursor.execute(sql)
mydb.commit()
