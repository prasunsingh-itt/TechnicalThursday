import pyodbc
class Admin:
    def input():
        print("Enter Id")
        Id = int(input())

    def connection():
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
        for x in myresult:
            print(str(x[0]))
            print(x[1])