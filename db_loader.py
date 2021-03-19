# load data from a raw mdb file and parse it for usable data to include later in the queries.
import csv, pyodbc

# set up some constants
MDB = 'C:/Users/MDT.Mohamed.Gueni/Desktop/WORKSPACE21/estmbx4.0/octoDB/MdtPartDB.mdb'
DRV = '{Microsoft Access Driver (*.mdb)}'
PWD = 'pw'

# connect to db
con = pyodbc.connect('DRIVER={};DBQ={};PWD={}'.format(DRV,MDB,PWD))
cur = con.cursor()

# run a query and get the results 
SQL = 'SELECT * FROM MCU;' # your query goes here
rows = cur.execute(SQL).fetchall()
print(rows)
cur.close()
con.close()

# you could change the mode from 'w' to 'a' (append) for any subsequent queries
with open('csv_db.csv', 'w') as fou:
    csv_writer = csv.writer(fou) # default field-delimiter is ","
    csv_writer.writerows(rows)