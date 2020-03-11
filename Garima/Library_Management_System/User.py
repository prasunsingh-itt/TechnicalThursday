import pyodbc
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