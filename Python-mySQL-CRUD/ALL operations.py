from DatabaseHelper import DatabaseHelper
Database=DatabaseHelper()


#A CRUD program to test the basic functionality for MYSQL by connecting it with PYTHON
def main():
    while True:
        print("\n\t\t\t\t*****WELCOME*******")
        print("\t\t\tPress 1 to Insert New User")
        print("\t\t\tPress 2 to Display ALL User")
        print("\t\t\tPress 3 to Delete ")
        print("\t\t\tPress 4 to Update a User")
        print("\t\t\tPress 5 to Exit")
        print()
        try:
            choice=int(input())
            if(choice==1):
                #insert user
                userID=int(input("Enter USERID :"))
                username=input("Enter USERNAME :")
                phone=int(input("Enter Phone number :"))
                Database.insert(userID,username,phone)
                pass
            elif choice==2:
                #display user
                Database.fetch_all()
                pass
            elif choice==3:
                #delete user
                print("\t\t\tPress 1 to Drop the Entire table")
                print("\t\t\tPress 2 to Delete a user with UserID ")
                print("\t\t\tPress 3 to exit ")
                try:
                    choice = int(input())
                    if(choice==1):
                        # Drop entire table
                        Database.DropEntireTable()
                        pass
                    elif choice==2:
                        userID=int(input("Enter USERID to which you want to DELETE"))
                        Database.delete_user(userID)
                        pass
                    elif choice == 3:
                        break
                    else:
                        print("\ninvalid ! Try again")
                except Exception as e:
                    print(e)
                    print("invalid details ! Try again")
                pass
            elif choice == 4:
                # update user
                userID=int(input("Enter USERID TO Which you want to Update "))
                username = input("Enter the NEW USERNAME :")
                phone = int(input("Enter THE NEW Phone number :"))
                Database.update(userID,username,phone)
                pass
            elif choice == 5:
                break
            else:
                print("\ninvalid ! Try again")
        except Exception as e:
            print(e)
            print("invalid details ! Try again")

if __name__=="__main__":
    main()