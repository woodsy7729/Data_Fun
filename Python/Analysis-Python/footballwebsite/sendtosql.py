import pyodbc
con = pyodbc.connect(Trusted_Connection='yes', driver = '{SQL Server}',server = 'JAMIES-LAPTOP\SQLEXPRESS' , database = 'master')

readfile = open("refineddata", "r")
for line in readfile:
    splitline = line.split(" ")
    "INSERT INTO footballdata(splitline[0], splitline[1],splitline[2],splitline[3])"
    '''.format?'''
