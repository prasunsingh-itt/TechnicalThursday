import pyodbc


DB = {'servername': 'PRASUN-ITT',
      'database': 'AdventureWorks2014'}


# create the connection
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + DB['servername'] + ';DATABASE=' + DB['database'] + ';Trusted_Connection=yes')



cursor = conn.cursor()
cursor.execute('SELECT * FROM [AdventureWorks2014].[Production].[Location]')

for row in cursor:
    print(row)