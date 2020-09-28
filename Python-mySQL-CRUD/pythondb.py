import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='2964')

mycursor=mydb.cursor()
mycursor.execute("create database python")
#mycursor.execute("show databases") #for o/p

for db in mycursor:
    print(db)