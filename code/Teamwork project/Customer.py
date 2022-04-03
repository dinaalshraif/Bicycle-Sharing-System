# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 21:16:04 2021

@author: dede_
"""
from tkinter import*
import sqlite3
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import datetime
import numpy as np

bs = sqlite3.connect('bikeshare.db')
cursor = bs.cursor()

ride_list = {"bikeid":0, "userid":0, "journy_length":0, "start_time":0, "end_time":0, "start_location": None, "end_location": None, "recipt":0, }
# Drop Down menue
def getSelectedRentLocation(selection):
    cursor.execute(f'''SELECT bike_status From bike WHERE location_id = '{selection}' ''')
    location_satus = []
    for x in cursor.fetchall():
        y = str(x) 
        x = y[2:-3]
        location_satus.append(x)
        
    if len(location_satus) == 0:
        cursor.execute(f''' UPDATE location SET location_satus = 'Empty' WHERE location_id = '{selection}' ''') 
        bs.commit()
        tkinter.messagebox.showwarning('warning','There is no available bike in the selected location\nPlease select another location ',icon= None,type= None)
        
    elif all(x != "normal" for x in location_satus):
        cursor.execute(f''' UPDATE location SET location_satus = 'No normal bikes' WHERE location_id = '{selection}' ''') 
        bs.commit()
        tkinter.messagebox.showwarning('warning','There is no available bike in the selected location\nPlease select another location ',icon= None,type= None)
   
    else: 
        availablBikeLabel = tk.Label(frame, text='You can start your bike journey from the selected location',font = ('Ink Free',15),bg='aliceblue',anchor='w')
        availablBikeLabel.place(x=400,y=150,width=620,height=60)
        
        cursor.execute(f'''SELECT bikeid From bike WHERE bike_status = 'normal' AND  location_id = '{selection}' ''')
        normalToworking = cursor.fetchone()
        normalToworking = normalToworking[0]
        
        ride_list['bikeid'] = normalToworking
        
        cursor.execute(f''' UPDATE bike SET bike_status ='working' WHERE bikeid = '{normalToworking}' ''') 
        bs.commit()
        
        bikeLabel = tk.Label(frame, text='Bike ID:',font = ('Ink Free',20),bg='aliceblue',anchor='w')
        bikeLabel.place(x=550,y=200,width=390,height=60)
        bikeIDLabel = tk.Label(frame, text= normalToworking ,font = ('Ink Free',20),bg='aliceblue',anchor='w')
        bikeIDLabel.place(x=690,y=200,width=590,height=60)
        
        rentBtn = tk.Button(frame, text='Rent', bg='white',font = ('Ink Free',10,'bold'), command = rent)
        rentBtn.place(x=600,y=250,width=100,height=40)
        rentBtn.focus()
        
        variable1 = StringVar(window2)
        variable1.set("Select Return location:") # default value
        locationMenu = OptionMenu(window2, variable1, 1, 2,3,4,5, command = getSelectedReturnLocation)
        locationMenu.place(x=550,y=370,width=250,height=30)
        ride_list['start_location'] = selection


def rent():
    
    startTimeLabel = tk.Label(frame, text='Start Time: ',font = ('Ink Free',20),bg='aliceblue',anchor='w')
    startTimeLabel.place(x=550,y=300,width=590,height=60)
     
    startTime = datetime.datetime.now()
    current_time = startTime.strftime("%H:%M:%S")
    ride_list ["start_time"] = current_time
    startTimeLabel2 = tk.Label(frame, text= current_time ,font = ('Ink Free',20),bg='aliceblue',anchor='w')
    startTimeLabel2.place(x=750,y=300,width=590,height=60)


def getSelectedReturnLocation(selection):
    
    cursor.execute(f'''SELECT bike_status From bike WHERE location_id = '{selection}' ''')
    location_satus = []
    for x in cursor.fetchall():
        y = str(x) 
        x = y[2:-3]
        location_satus.append(x)
          
    cursor.execute(f'''SELECT bike_status From bike WHERE location_id = '{selection}'  AND  bike_status ='normal' ''')
    location_satus_normal = []
    for x in cursor.fetchall():
        y = str(x) 
        x = y[2:-3]
        location_satus_normal.append(x)
        
    cursor.execute(f'''SELECT bike_status From bike WHERE location_id = '{selection}'  AND  bike_status ='defective' ''')
    location_satus_defective = []
    for x in cursor.fetchall():
        y = str(x) 
        x = y[2:-3]
        location_satus_defective.append(x)
        
    if len(location_satus_normal) + len(location_satus_defective) > 100:
        cursor.execute(f''' UPDATE location SET location_satus = 'Full' WHERE location_id = '{selection}' ''') 
        bs.commit()
        tkinter.messagebox.showwarning('warning','There is no available parking in the selected location\nPlease select another location ',icon= None,type= None)
    else: 
        ride_list["end_location"] = selection
        bs.commit()
        availablBikeLabel = tk.Label(frame, text='You can End your bike journey at the selected location',font = ('Ink Free',15),bg='aliceblue',anchor='w')
        availablBikeLabel.place(x=400,y=400,width=600,height=60)
        
        endTimeLabel = tk.Label(frame, text='End Time: ',font = ('Ink Free',20),bg='aliceblue',anchor='w')
        endTimeLabel.place(x=550,y=450,width=590,height=60)
     
        endtTime = datetime.datetime.now()
        current_time = endtTime.strftime("%H:%M:%S")
        ride_list["end_time"] = current_time
        endTimeLabel2 = tk.Label(frame, text= current_time ,font = ('Ink Free',20),bg='aliceblue',anchor='w')
        endTimeLabel2.place(x=750,y=450,width=590,height=60)
        print(ride_list) 
    
def login():
    # get user inputs name and password
    name = name_box.get()
    password = password_box.get()
    # clear the text boxes after press save 
    password_box.delete(0, END)
    password_box.focus()
    name_box.delete(0, END)
    name_box.focus()
    
    cursor.execute(f'''SELECT user_name From user ''')
    username_list = []
    for x in cursor.fetchall():
        y = str(x) 
        x = y[2:-3]
        username_list.append(x)
    
    
    if any( x == name for x in username_list):
        window.destroy()
        rentlabel = tk.Label(frame, text='Rent a Bike',font = ('Ink Free',40,'bold'),bg='aliceblue',anchor='w')
        rentlabel.place(x=500,y=30,width=400,height=60)        
        variable = StringVar(window2)
        variable.set("Select location:") # default value
        locationMenu = OptionMenu(window2, variable, 1, 2,3,4,5, command = getSelectedRentLocation)
        locationMenu.place(x=550,y=100,width=250,height=30)
        
        cursor.execute(f'''SELECT  userid From user  WHERE user_name = '{name}' ''')
        userId = cursor.fetchall()
        userId = userId[0][0]
        ride_list["userid"] = userId
    
    else:
        tkinter.messagebox.showwarning('warning','Invalid username, If you dont have account please register ',icon= None,type= None)
       
        
def register():
    # get user inputs name and password
    name = name_box.get()
    password = password_box.get()
    # clear the text boxes after press save 
    password_box.delete(0, END)
    password_box.focus()
    name_box.delete(0, END)
    name_box.focus()
    
    #Select all usernames in the database 
    cursor.execute('SELECT user_name FROM user') 
    # Save all the usernames in the array called usernameList
    usernameList = np.array(cursor.fetchall())
    #check if any of the password digits is a number
    pass_number = any(char.isdigit() for char in password)
    # ignore password has length less than 8
    if len(password) < 8 : 
        tkinter.messagebox.showwarning('warning','Invalid Password, password sholud contain at least 8 digits ',icon= None,type= None)
    # ignore password if it has not contained any number
    elif pass_number == False:
        tkinter.messagebox.showwarning('warning','Invalid Password, password sholud contain at least one num ',icon= None,type= None)
    else:
        cursor.execute("""INSERT INTO user(user_name, password) 
        VALUES(?, ?)""", (name, password))
        bs.commit() 
        window.destroy()
        rentlabel = tk.Label(frame, text='Rent a Bike',font = ('Ink Free',40,'bold'),bg='aliceblue',anchor='w')
        rentlabel.place(x=500,y=30,width=400,height=60)        
        variable = StringVar(window2)
        variable.set("Select location:") # default value
        locationMenu = OptionMenu(window2, variable, 1, 2,3,4,5, command = getSelectedRentLocation)
        locationMenu.place(x=550,y=100,width=250,height=30)
        
        


    
window = Tk()
window.title("Login Page")


window.geometry('1300x880+390+75')
frame = tk.Frame(window, bg='aliceblue')
frame.place(x=0,y=0,width=1300,height=880)
loginlabel = tk.Label(frame, text='Login / Register',font = ('Ink Free',40,'bold'),bg='aliceblue',anchor='w')
loginlabel.place(x=300,y=30,width=900,height=100)

label1 = Label(frame, text='Username: ',font = ('Ink Free',20,'bold'),bg='aliceblue',anchor='w')
label1.place(x = 300, y = 200, height = 50 , width = 300)

name_box = Entry(text = 0)
name_box.place(x = 620, y = 200, height = 25 , width = 150)
name_box.focus()

label2 = Label(frame, text='Password: ',font = ('Ink Free',20,'bold'),bg='aliceblue',anchor='w')
label2.place(x = 300, y = 300, height = 50 , width = 200)

password_box = Entry(text = 1)
password_box.place(x = 620, y = 300, height = 25 , width = 150)
password_box.focus()

button1 = tk.Button(frame, text='Login', bg='white',font = ('Ink Free',10,'bold'), command = login)
button1.place(x = 500, y = 500, height = 25 , width = 90)

button1 = tk.Button(frame, text='Register', bg='white',font = ('Ink Free',10,'bold'), command = register)
button1.place(x = 700, y = 500, height = 25 , width = 90)


window2 = Tk()
window2.title("Rent a Bike")
window2.geometry('1300x880+390+75')
frame = tk.Frame(window2, bg='aliceblue')
frame.place(x=0,y=0,width=1300,height=880)

window2.mainloop()






