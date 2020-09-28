import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='2964',database='python')

mycursor=mydb.cursor()

sqlform="insert into py(name,number) values(%s,%s)"
xyz=[("amit",1),("aniket",2),("mitra",3)]
mycursor.executemany(sqlform,xyz)
mydb.commit()

