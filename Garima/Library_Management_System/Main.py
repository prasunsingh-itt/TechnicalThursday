import pyodbc
class Admin:
    def connection():
        Id = int(input("Enter Id"))
        conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=GARIMA-ARORA;'
                        'Database=LibraryManagementSystem;'
                        'Trusted_Connection=yes;')
        cursor = conn.cursor()
        cursor.execute("select Id , Name from Authenticate where id = "+ str(Id))
        myresult = cursor.fetchall()
        row_count = cursor.rowcount
        print ("number of affected rows: {}".format(row_count))
        if row_count == 0:
            print ("Not a Valid User")
        if row_count == -1:
            print("jhshdv")

class User:
    def addUser():
        print("Enter Id")
        Id = int(input())
        print("Enter Name")
        Name = input()
        print("Enter Email")
        Email = input()
        print("Enter Availability of book")
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
        print("1.Admin\n 2.Librarian\n 3.Student")
        Input = int(input())
        if Input == 1:
            Admin.connection()
        if Input == 2:
            option = int(input("Select Option:\n1.Get Profile of User\n2.Get Details of Book\n3.search Book"))
            if option == 1:
                User.showUserDetails()
            if option == 2:
                Book.showBookDetails()
            if option == 3:
                Book.searchBook(int(input("Enter Id")))
                
Object = Main()
Object.__init__()