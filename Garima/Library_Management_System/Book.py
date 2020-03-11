import pyodbc

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