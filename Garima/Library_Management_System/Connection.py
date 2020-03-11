import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=GARIMA-ARORA;'
                      'Database=AdventureWorks2014;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT top 100 * FROM [AdventureWorks2014].[HumanResources].[EmployeeDepartmentHistory]')

for row in cursor:
    print(row)