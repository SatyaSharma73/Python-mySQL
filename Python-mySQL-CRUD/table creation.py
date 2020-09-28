import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='2964',database='python')

mycursor=mydb.cursor()
mycursor.execute("create table py(name varchar(200),number int(10))")
#mycursor.execute("show tables") #for o/p

#for tb in mycursor:
   # print(tb)