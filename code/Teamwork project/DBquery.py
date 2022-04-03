#This file is just for querying information of tables in database
#At the end of this file is an example to transfer datetime from database to python
##I think it may help a lot when caculating the riding time and income/charge
import sqlite3
import datetime

bs = sqlite3.connect('bikeshare.db')
cursor = bs.cursor()

cursor.execute(f'''SELECT * From ride''')
for x in cursor.fetchall():
    print(x)

cu
bs.close()