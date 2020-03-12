import pyodbc
class Admin:
    def connection(Id):
        conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=GARIMA-ARORA;'
                        'Database=LibraryManagementSystem;'
                        'Trusted_Connection=yes;')
        cursor = conn.cursor()
        cursor.execute("select Id , Name from Authenticate where id = "+ str(Id))
        myresult = cursor.fetchall()
        row_count = cursor.rowcount
#       print ("number of affected rows: {}".format(row_count))
        if row_count == 0:
            print ("Not a Valid User")
            exit()
        if row_count == -1:
            print("You are authenticated User:\nSelect Option:")
            print("\n1.Add Book\n2.Update Book Details\n3.Add User\n4.Delete User")
            selectOption = int(input("\nEnter Input"))
            if selectOption == 1:
                Book.addBook()
                exit()
            if selectOption == 2:
                print("update")
            if selectOption == 3:
                User.addUser()
                exit()
            if selectOption == 4:
                User.DeleteUser()
                exit()
            

class User:
    def addUser():
        print("Enter Id")
        Id = int(input())
        print("Enter Name")
        Name = input()
        print("Enter Email")
        Email = input()
        print("Availability")
        isActive = int(input())
        conn = pyodbc.connect('Driver={SQL Server};'
                            'Server=GARIMA-ARORA;'
                            'Database=LibraryManagementSystem;'
                            'Trusted_Connection=yes;')
        cursor = conn.cursor()
        SQLCommand = ("INSERT INTO UserDetails(Id,Name, email, isActive) VALUES (?,?,?,?)")
        Values = (Id,Name,Email,isActive)
        cursor.execute(SQLCommand,Values)
        conn.commit()
        print("1 record inserted, ID:", Id)
    
    def showUserDetails():
        conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=GARIMA-ARORA;'
                        'Database=LibraryManagementSystem;'
                        'Trusted_Connection=yes;')
        cursor = conn.cursor()
        cursor.execute("select * from UserDetails")
        myresult = cursor.fetchall()
        for row in myresult:
            print(row)
        
    def DeleteUser():
        print("Enter Id of user you want to delete:")
        Id = int(input())
        conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=GARIMA-ARORA;'
                        'Database=LibraryManagementSystem;'
                        'Trusted_Connection=yes;')
        cursor = conn.cursor()
        cursor.execute("delete from UserDetails where Id =" + str(Id))
        conn.commit()
        print("1 record deleted, ID:", Id)

class Book:
    def addBook():
        print("Enter Id")
        Id = int(input())
        print("Enter Title")
        Title = input()
        print("Enter Author")
        Author = input()
        print("Enter Status")
        Status = int(input())
        print("Enter Published Date")
        Date = input()
        print("Enter Price")
        Price = float(input())
        conn = pyodbc.connect('Driver={SQL Server};'
                            'Server=GARIMA-ARORA;'
                            'Database=LibraryManagementSystem;'
                            'Trusted_Connection=yes;')
        cursor = conn.cursor()
        SQLCommand = ("INSERT INTO Book(Id,Title, Author,Status,Date, Price) VALUES (?,?,?,?,?,?)")
        Values = (Id,Title,Author,Status,Date,Price)
        cursor.execute(SQLCommand,Values)
        conn.commit()
        print("1 record inserted, ID:", Id)
    
    def showBookDetails():
        conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=GARIMA-ARORA;'
                        'Database=LibraryManagementSystem;'
                        'Trusted_Connection=yes;')
        cursor = conn.cursor()
        cursor.execute("select * from Book")
        myresult = cursor.fetchall()
        for row in myresult:
            print(row)
    
    def searchBook(Id):
        conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=GARIMA-ARORA;'
                        'Database=LibraryManagementSystem;'
                        'Trusted_Connection=yes;')
        cursor = conn.cursor()
        cursor.execute("select * from Book where Id =" + str(Id))
        myresult = cursor.fetchall()
        for row in myresult:
            print(row)

class Main:
    def __init__(self):
        print("Select Profile:")
        print("\n1.Admin\n2.Librarian\n3.Student")
        Input = int(input())
        if Input == 1:
            Admin.connection(int(input("\nEnter Id")))
        if Input == 2:
            option = int(input("Select Option:\n1.Get Profile of User\n2.Get Details of Book\n3.search Book"))
            if option == 1:
                User.showUserDetails()
                exit()
            if option == 2:
                Book.showBookDetails()
                exit()
            if option == 3:
                Book.searchBook(int(input("\nEnter Id")))
                exit()
                
Object = Main()
Object.__init__()