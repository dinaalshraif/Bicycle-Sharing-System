import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import sqlite3
import datetime

bs = sqlite3.connect('bikeshare.db')
cursor = bs.cursor()

ride_list = {"bikeid":0, "userid":0, "journy_length":0, "start_time":0, "end_time":0, "start_location": None, "end_location": None, "recipt":0, }
ride_list1={"start_time1":0, "end_time1":0,"user_name":0}
class Report(object):
    def __init__(self, window):
        self.window = window
        self.window.title("BikeShare - Report Failure Information")
        self.window.geometry('1300x880+390+75')
        self.frame = tk.Frame(self.window, bg='aliceblue')
        self.frame.place(x=0,y=0,width=1300,height=880)

  
        tk.Label(self.window, text='The Bike ID:', font = ('Ink Free',35),bg='aliceblue',anchor='w').place(x = 150, y = 150)
        self.id_input = tk.Entry(self.window)
        self.id_input.place(x =550, y = 165, width=200, height = 30)


        self.submit_button = tk.Button(self.window, text = "Submit", bg='white',font = ('Ink Free',15,'bold'), command = self.Submit).place(x = 900, y = 160, width=80, height = 40)
        self.return_button = tk.Button(self.window, text = "Return", bg='white',font = ('Ink Free',15,'bold'), command = self.Return).place(x = 1000, y = 700, width=80, height = 40)

    def Submit(self):
        report_id = self.id_input.get() 
        cursor.execute(f'''UPDATE bike SET bike_status = 'defective' where bikeid='{report_id}' ''')
        tk.messagebox.showinfo(title='Thank you',message='Submit Successfully!')
        self.id_input.delete(0, tk.END)
        bs.commit()    
     
    def Return(self):
        self.frame.destroy()
        MainMenu(self.window)
 

class Confirm():
    def __init__(self, window):
        self.window = window
        self.window.title("Login Page")
        self.window.geometry('1300x880+390+75')
        self.frame = tk.Frame(self.window, bg='aliceblue')
        self.frame.place(x=0,y=0,width=1300,height=880)
        self.loginlabel = tk.Label(self.frame, text='Login / Register',font = ('Ink Free',40,'bold'),bg='aliceblue',anchor='w')
        self.loginlabel.place(x=300,y=30,width=900,height=100)
        
        self.label1 = tk.Label(self.frame, text='Username: ',font = ('Ink Free',20,'bold'),bg='aliceblue',anchor='w')
        self.label1.place(x = 300, y = 200, height = 50 , width = 300)
        
        self.name_box = tk.Entry(self.frame, text = 0)
        self.name_box.place(x = 620, y = 200, height = 25 , width = 150)
        self.name_box.focus()
        self.label2 = tk.Label(self.frame, text='Password: ',font = ('Ink Free',20,'bold'),bg='aliceblue',anchor='w')
        self.label2.place(x = 300, y = 300, height = 50 , width = 200)
        
        self.password_box = tk.Entry(self.frame, text = 1)
        self.password_box.place(x = 620, y = 300, height = 25 , width = 150)
        self.password_box.focus()
        
        self.button1 = tk.Button(self.frame, text='Login', bg='white',font = ('Ink Free',10,'bold'), command = self.login)
        self.button1.place(x = 500, y = 500, height = 25 , width = 90)
        self.button2 = tk.Button(self.frame, text='Register', bg='white',font = ('Ink Free',10,'bold'), command = self.register)
        self.button2.place(x = 700, y = 500, height = 25 , width = 90)
    
    def login(self):
        # get user inputs name and password
        name = self.name_box.get()
        password = self.password_box.get()
        # clear the text boxes after press save
        self.password_box.delete(0, tk.END)
        self.password_box.focus()
        self.name_box.delete(0, tk.END)
        self.name_box.focus()
    
        cursor.execute(f'''SELECT user_name From user ''')
        username_list = []
        for x in cursor.fetchall():
            y = str(x) 
            x = y[2:-3]
            username_list.append(x)

        if any( x == name for x in username_list):
            cursor.execute(f'''SELECT  userid From user  WHERE user_name = '{name}' ''')
            userId = cursor.fetchall()
            userId = userId[0][0]
            ride_list["userid"] = userId
            ride_list1["user_name"]=name
            
            cursor.execute(f'''SELECT password From user WHERE  user_name = '{name}' AND userid = '{userId}'  ''')
            userPassword = cursor.fetchall()
            userPassword1 = userPassword[0][0]
            #print(password)
            if (userPassword1 != password ):
                tkinter.messagebox.showwarning('warning','Invalid Password, If you dont have account please register ',icon= None,type= None)
            else:
                 self.frame.destroy()
                 MainMenu(self.window)         
        else: 
            tkinter.messagebox.showwarning('warning','Invalid username, If you dont have account please register ',icon= None,type= None)
    
    def register(self):
        # get user inputs name and password
        name = self.name_box.get()
        password = self.password_box.get()
        # clear the text boxes after press save 
        self.password_box.delete(0, tk.END)
        self.password_box.focus()
        self.name_box.delete(0, tk.END)
        self.name_box.focus()
    
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
            cursor.execute(f'''SELECT  userid From user  WHERE user_name = '{name}' ''')
            userId = cursor.fetchall()
            userId = userId[0][0]
            ride_list["userid"] = userId
            ride_list1["user_name"]=name
            cursor.execute(f'''UPDATE user SET account_balance == 0 WHERE user_name = '{name}' ''')
            bs.commit()
            self.frame.destroy()
            MainMenu(self.window)
            
            


class MainMenu():
    def __init__(self,window):
        self.window = window
        self.window.title("Main Menu")
        self.window.geometry('1300x880+390+75')
        self.frame = tk.Frame(self.window, bg='aliceblue')
        self.frame.place(x=0,y=0,width=1300,height=880)
        self.reportBtn = tk.Button(self.frame, text='Report', bg='white',font = ('Ink Free',20,'bold'), command=self.report)
        self.reportBtn.place(x=500,y=140,width=100,height=30)
        self.rentBtn = tk.Button(self.frame, text='Rent', bg='white',font = ('Ink Free',20,'bold'), command=self.rent)
        self.rentBtn.place(x=500,y=340,width=100,height=30)
        self.rentBtn = tk.Button(self.frame, text='Check My Account', bg='white',font = ('Ink Free',20,'bold'), command=self.account)
        self.rentBtn.place(x=400,y=540,width=300,height=30)
    def report(self):
        self.frame.destroy()
        Report(self.window)
    
    def rent(self):
        self.frame.destroy()
        RentMenu(self.window)
    
    def account(self):
        self.frame.destroy()
        BankAccount(self.window)

class BankAccount():
    def __init__(self,window):
        self.window = window
        self.window.title("Check My Account Balance")
        self.window.geometry('1300x880+390+75')
        self.frame = tk.Frame(self.window, bg='aliceblue')
        self.frame.place(x=0,y=0,width=1300,height=880) 

        self.banklabel = tk.Label(self.frame, text='Check my account',font = ('Ink Free',40,'bold'),bg='aliceblue',anchor='w')
        self.banklabel.place(x=500,y=30,width=400,height=60)
        
        self.payBtn2 = tk.Button(self.frame, text='Check', bg='white',font = ('Ink Free',10,'bold'), command =self.Bankaccount)
        self.payBtn2.place(x=530,y=100,width=300,height=40)
        self.return_button = tk.Button(self.window, text = "Return", bg='white',font = ('Ink Free',15,'bold'), command = self.Return).place(x = 1000, y = 700, width=80, height = 40)
    
    def Return(self):
        self.frame.destroy()
        MainMenu(self.window)


        
    def Bankaccount(self): 
        name = ride_list1["user_name"]
        cursor.execute(f'''SELECT account_balance From user where user_name= '{name}' ''')
        for x in cursor.fetchall():
            #print(x)
            #print(type(x))
            a=x[0]
            a = round(a,2)
            b=str(a)
            #print(a)
            ride_list["account_balance"]=a
            #print( ride_list["account_balance"])
            if a==0:
                self.banklabel = tk.Label(self.frame, text="Your account balance is 0",font = ('Ink Free',40,'bold'),bg='aliceblue',anchor='w')
                self.banklabel.place(x=400,y=150,width=700,height=60) 
                tkinter.messagebox.showwarning('warning','You have no money in your account,please charge your account',icon= None,type= None)
                
            else:
                self.banklabel1 = tk.Label(self.frame, text="Your account balance is "+b+" pounds",font = ('Ink Free',30,'bold'),bg='aliceblue',anchor='w')
                self.banklabel1.place(x=350,y=150,width=800,height=60)
            self.payBtn1 = tk.Button(self.frame, text='charge money', bg='white',font = ('Ink Free',10,'bold'), command =self.charge)
            self.payBtn1.place(x=530,y=220,width=300,height=40)
           
    def charge(self):
            name = ride_list1["user_name"]
            user_account=ride_list["account_balance"]+10
            user_account = round(user_account,2)
            user_account1=str(user_account)
            #print(type(user_account))
            ride_list["account_balance"]=user_account
            #print(ride_list["account_balance"])
            ###cursor.execute("""INSERT INTO user(account_balance) VALUES(?)""", (user_account))
           
            cursor.execute(f'''UPDATE user SET account_balance = {user_account} where user_name= '{name}' ''')
            bs.commit()
            self.banklabel2 = tk.Label(self.frame, text="Now you have "+user_account1+"pounds",font = ('Ink Free',30,'bold'),bg='aliceblue',anchor='w')
            self.banklabel2.place(x=400,y=270,width=700,height=60)
            
class ReportMenu():
    def __init__(self,window):
        self.window = window
        self.window.title("Report Menu")
        self.window.geometry('1300x880+390+75')
        self.frame = tk.Frame(self.window, bg='aliceblue')
        self.frame.place(x=0,y=0,width=1300,height=880)
        

class RentMenu():
    def __init__(self,window):
        self.window = window
        self.window.title("Rent a Bike")
        self.window.geometry('1300x880+390+75')
        self.frame = tk.Frame(self.window, bg='aliceblue')
        self.frame.place(x=0,y=0,width=1300,height=880)
        self.rentlabel = tk.Label(self.frame, text='Rent a Bike',font = ('Ink Free',40,'bold'),bg='aliceblue',anchor='w')
        self.rentlabel.place(x=500,y=30,width=400,height=60)        
        self.variable = tk.StringVar(self.window)
        self.variable.set("Please Select a location to rent a bike:") # default value
        self.locationMenu = tk.OptionMenu(self.window, self.variable, 1, 2,3,4,5, command = self.getSelectedRentLocation)
        self.locationMenu.place(x=530,y=100,width=350,height=30)
        self.return_button = tk.Button(self.window, text = "Return", bg='white',font = ('Ink Free',15,'bold'), command = self.Return).place(x = 1000, y = 700, width=80, height = 40)
    
    def Return(self):
        self.frame.destroy()
        MainMenu(self.window)



    def getSelectedRentLocation(self,selection):
        cursor.execute(f'''SELECT bike_status From bike WHERE location_id = '{selection}' ''')
        location_satus = []
        for x in cursor.fetchall():
            y = str(x) 
            x = y[2:-3]
            location_satus.append(x)
        
        if len(location_satus) == 0:
            cursor.execute(f''' UPDATE location SET location_status = 'Empty' WHERE location_id = '{selection}' ''') 
            bs.commit()
            tkinter.messagebox.showwarning('warning','There is no available bike in the selected location\nPlease select another location ',icon= None,type= None)
        elif all(x != "normal" for x in location_satus):
            cursor.execute(f''' UPDATE location SET location_status = 'No normal bikes' WHERE location_id = '{selection}' ''') 
            bs.commit()
            tkinter.messagebox.showwarning('warning','There is no available bike in the selected location\nPlease select another location ',icon= None,type= None)
        else: 
            availablBikeLabel = tk.Label(self.frame, text='You can start your bike journey from the selected location',font = ('Ink Free',15),bg='aliceblue',anchor='w')
            availablBikeLabel.place(x=400,y=150,width=620,height=60)
        
            cursor.execute(f'''SELECT bikeid From bike WHERE bike_status = 'normal' AND  location_id = '{selection}' ''')
            normalToworking = cursor.fetchone()
            normalToworking = normalToworking[0]
        
            ride_list['bikeid'] = normalToworking
            #print(type(normalToworking))
        
            cursor.execute(f''' UPDATE bike SET bike_status ='working' WHERE bikeid = '{normalToworking}' ''') 
            bs.commit()
        
            self.bikeLabel = tk.Label(self.frame, text='Bike ID:',font = ('Ink Free',20),bg='aliceblue',anchor='w')
            self.bikeLabel.place(x=550,y=200,width=390,height=60)
            self.bikeIDLabel = tk.Label(self.frame, text= normalToworking ,font = ('Ink Free',20),bg='aliceblue',anchor='w')
            self.bikeIDLabel.place(x=690,y=200,width=590,height=60)
        
            self.rentBtn = tk.Button(self.frame, text='Rent', bg='white',font = ('Ink Free',10,'bold'), command = self.startTime)
            self.rentBtn.place(x=600,y=250,width=100,height=40)
            self.rentBtn.focus()
            ride_list['start_location'] = selection
            #print(type(selection))
            
        

    def startTime(self):
        self.startTimeLabel = tk.Label(self.frame, text='Start Time: ',font = ('Ink Free',20),bg='aliceblue',anchor='w')
        self.startTimeLabel.place(x=550,y=300,width=590,height=60)
        
        startTime = datetime.datetime.utcnow()
        current_start = startTime.strftime("%Y-%m-%d %H:%M:%S")
        startTime = datetime.datetime.strptime(current_start, '%Y-%m-%d %H:%M:%S')
        #print('startTime',startTime,' ',type(startTime))
        #print(current_start)
        ride_list ["start_time"] =startTime
        ride_list1 ["start_time1"] = startTime
        #print(type(current_start))
            
        self.startTimeLabel2 = tk.Label(self.frame, text= current_start ,font = ('Ink Free',20),bg='aliceblue',anchor='w')
        self.startTimeLabel2.place(x=750,y=300,width=590,height=60)
        self.returnBike()
        
    def returnBike(self):
        self.variable1 = tk.StringVar(self.window)
        self.variable1.set("Please Select a location to return the bike:") # default value
        self.locationMenu = tk.OptionMenu(self.window, self.variable1, 1, 2,3,4,5, command = self.getSelectedReturnLocation)
        self.locationMenu.place(x=530,y=370,width=350,height=30)

    def getSelectedReturnLocation(self, selection):
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
        
        if len(location_satus_normal) + len(location_satus_defective) > 200:
            cursor.execute(f''' UPDATE location SET location_status = 'Full' WHERE location_id = '{selection}' ''') 
            bs.commit()
            tkinter.messagebox.showwarning('warning','There is no available parking in the selected location\nPlease select another location ',icon= None,type= None)
        else: 
            ride_list["end_location"] = selection
            #print(type(selection))
            bs.commit()
            availablBikeLabel = tk.Label(self.frame, text='You can End your bike journey at the selected location',font = ('Ink Free',15),bg='aliceblue',anchor='w')
            availablBikeLabel.place(x=400,y=400,width=600,height=60)
        
            endTimeLabel = tk.Label(self.frame, text='End Time: ',font = ('Ink Free',20),bg='aliceblue',anchor='w')
            endTimeLabel.place(x=550,y=450,width=590,height=60)
     
            endtTime = datetime.datetime.utcnow()
            #current_time = endtTime.strftime("%H:%M:%S")
            current_time = endtTime.strftime("%Y-%m-%d %H:%M:%S")
            endtTime = datetime.datetime.strptime(current_time, '%Y-%m-%d %H:%M:%S')
            #print('endTime',endtTime,' ',type(endtTime))
            
            ride_list["end_time"] =  endtTime
            ride_list1["end_time1"] = endtTime
            #print(type(current_time))
            endTimeLabel2 = tk.Label(self.frame, text= current_time,font = ('Ink Free',20),bg='aliceblue',anchor='w')
            endTimeLabel2.place(x=750,y=450,width=590,height=60)
            self.payBtn = tk.Button(self.frame, text='make a payment', bg='white',font = ('Ink Free',10,'bold'), command =self.payment)
            self.payBtn.place(x=530,y=550,width=300,height=40)
            cursor.execute(f''' UPDATE bike SET location_id = {ride_list["end_location"]} WHERE bikeid = {ride_list["bikeid"]} ''') 
            cursor.execute(f''' UPDATE bike SET bike_status = 'normal' WHERE bikeid = {ride_list["bikeid"]} ''')
            bs.commit()
            
    def payment(self):
######get the starttime and endtime from database
        name = ride_list1["user_name"]
        cursor.execute(f'''SELECT account_balance From user where user_name= '{name}' ''')
        for x in cursor.fetchall():
            #print(x)
            #print(type(x))
            a=x[0]
            b=str(a)
            #print(a)
            ride_list["account_balance"]=a
            #print( ride_list["account_balance"])
        interval=ride_list1["end_time1"]-ride_list1["start_time1"]
        paytime=interval.total_seconds()
        #print('ridelist start',ride_list1["start_time1"])
        #print('ridelist end',ride_list1["end_time1"])
        #print('interval',interval)
        #print('paytime',paytime)
        pay1=str(paytime)
        ride_list["journy_length"]= pay1
        #print(type(pay1))
        self.paytimelabel =tk.Label(self.frame, text='Using time in total is：'+pay1+'seconds',font = ('Ink Free',15),bg='aliceblue',anchor='w')
        self.paytimelabel.place(x=400,y=590,width=400,height=60) 
    
####half pounds each 30minutes
        charge=paytime*0.02
        charge=round(charge,3)
        charges=str(charge)
        ride_list ["recipt"]=charge
        #print(type(charge))
        #print(ride_list)
        self.paytimelabel2 =tk.Label(self.frame, text='Your charge is：'+charges+'pounds',font = ('Ink Free',15),bg='aliceblue',anchor='w')
        self.paytimelabel2.place(x=400,y=650,width=400,height=60)
        if a>=charge:
            user_account=ride_list["account_balance"]-charge
            user_account1=str(user_account)
            #print(type(user_account))
            ride_list["account_balance"]=user_account
            #print(ride_list["account_balance"])
            tk.messagebox.showinfo(title='Payment Successful',message='See You Nexttime!')
        else:
            tkinter.messagebox.showwarning('warning','You have no money in your account,please charge your account',icon= None,type= None)
            ###cursor.execute("""INSERT INTO user(account_balance) VALUES(?)""", (user_account))
           
        cursor.execute(f'''UPDATE user SET account_balance = {user_account} where user_name= '{name}' ''')
        bs.commit()
        cursor.execute(f'''INSERT INTO ride (bikeid, userid, journy_length, start_time,end_time,start_location,end_location,recipt) 
  VALUES({ride_list['bikeid']},{ride_list['userid']},{ride_list['journy_length']},'{ride_list['start_time']}',
'{ride_list['end_time']}',{ride_list['start_location']},{ride_list['end_location']},{ride_list['recipt']})''')
       
        bs.commit()
#main
if __name__ == '__main__': 
    window = tk.Tk()
    #window.resizable(0,0)
    Confirm(window)
    window.mainloop()
    
bs.close()