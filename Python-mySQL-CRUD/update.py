import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='2964',database='satyadb')

mycursor=mydb.cursor()

sql="UPDATE xyz SET sal=70000 where name='satya'"
mycursor.execute(sql)
mydb.commit()
