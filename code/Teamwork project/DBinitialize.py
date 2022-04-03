#This is an initializing py file for testing operator's function
#I initialize the bikes table with 500 bikes (100bikes in each location)
#I also set some of these bikes working or defective when initializing the bikes table
##so that I can test repair&move funcion 
#This file only needs to be run for one time   

import sqlite3

bs = sqlite3.connect('bikeshare.db')
cursor = bs.cursor()
cursor.execute(f'''UPDATE user SET account_balance == 0 ''')
bs.commit()
##insert 5 locations to location
for i in range(1,6):
    cursor.execute(f'''INSERT INTO location(location_id)values({i})''')
    
for i in range(1,6):
    cursor.execute(f''' UPDATE location SET location_number = '{i}' WHERE location_id= '{i}' ''')

##insert 100 bikes to each location
for i in range(100):
   cursor.execute(f'''INSERT INTO bike(bikeid,location_id,bike_status)values({i},1,'normal')''')
for i in range(100,200):
    cursor.execute(f'''INSERT INTO bike(bikeid,location_id,bike_status)values({i},2,'normal')''')
for i in range(200,300):
    cursor.execute(f'''INSERT INTO bike(bikeid,location_id,bike_status)values({i},3,'normal')''')
for i in range(300,400):
    cursor.execute(f'''INSERT INTO bike(bikeid,location_id,bike_status)values({i},4,'normal')''')
for i in range(400,500):
    cursor.execute(f'''INSERT INTO bike(bikeid,location_id,bike_status)values({i},5,'normal')''')

##set some of bikes defective/working for testing
for i in range(0,500,4):
    order = f'''UPDATE bike SET bike_status = 'defective' WHERE bikeid = {i}'''
    cursor.execute(order)
for i in range(0,500,6):
    order = f'''UPDATE bike SET bike_status = 'working' WHERE bikeid = {i}'''
    cursor.execute(order)
for i in range(1,6):
    cursor.execute(f'''UPDATE  location SET location_satus = 'Available' WHERE location_id = {i}''')
bs.commit()

##display the initialized bike&location table
cursor.execute(f'''SELECT * From location''')
for x in cursor.fetchall():
    print(x)
cursor.execute(f'''SELECT * From bike''')
for x in cursor.fetchall():
    print(x)
    


bs.close()