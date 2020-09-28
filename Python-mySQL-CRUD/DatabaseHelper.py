import mysql.connector as connector
class DatabaseHelper:
    def __init__(self):
      #passwd may varry for different users rest remain the same
      # Change Database Value to Create a NEW DATABASE

      self.con= connector.connect(host='localhost', user='root', passwd='2964',database='python')

      query='create table if not exists user(userid int primary key,username varchar(200),phone int(10))'
      #here user is the table name with a basic entities like userid,username,phone
      #you can modify it according to your need
      cur=self.con.cursor()
      cur.execute(query)

    #Insert
    def insert(self,userID,username,phone):
        query = "insert into user(userID,username,phone) values({},'{}',{})".format(
            userID,username,phone)

        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("******Sucessfull******")

    #FetchAll
    def fetch_all(self):
        query="select * from user"
        cur=self.con.cursor()
        cur.execute(query)
        print()
        for row in cur:
            print(row)

       #use the below code to get the results in grouped form for a perticular userID
            #print("UserID :",row[0])
            #print("Username :", row[1])
            #print("Phone :", row[1])

    #Delete
    def delete_user(self,userID):
        query="delete from user where userID={}".format(userID)
        #query can be change according your need
        cur=self.con.cursor()
        cur.execute(query)
        print("Deleted",userID,"******Sucessfull******")

        self.con.commit()

    #update
    def update(self,userID,newusername,newphone):
        query="UPDATE user SET username='{}' ,phone={} where userID={}".format(newusername,newphone,userID)
        cur=self.con.cursor()

        cur.execute(query)
        print("Update ******Sucessfull******")
        self.con.commit()

    #Drop the entire table
    def DropEntireTable(self):
        query="Drop table user"
        cur=self.con.cursor()
        cur.execute(query)
        print(" Dropped The Entire Table ")
        self.con.commit()

    #Drop the Entire Row
    def DeleteEntireRow(self,userId):
        query = "Delete from user where userID={}".format(userId)
        cur = self.con.cursor()
        cur.execute(query)
        print("Deleted the Row Where userID =:",userId )
        self.con.commit()