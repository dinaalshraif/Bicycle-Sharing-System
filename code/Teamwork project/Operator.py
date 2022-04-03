import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import sqlite3

bs = sqlite3.connect('bikeshare.db')
cursor = bs.cursor()

#confirm window to check password
class Confirm():
    def __init__(self, window):
        self.window = window
        self.window.title('BikeShare - Operators:Login')
        self.window.geometry('800x480+120+75')
        self.frame = tk.Frame(self.window,bg='aliceblue')
        self.frame.place(x=0,y=0,width=800,height=480)
        
        self.hintlabel = tk.Label(self.frame, text='Welcome! ',font = ('Ink Free',40,'bold'),bg='aliceblue',anchor='w')
        self.hintlabel.place(x=200,y=120,width=200,height=60)
        self.hintlabel = tk.Label(self.frame, text='Password: ',font = ('Ink Free',20,'bold'),bg='aliceblue',anchor='w')
        self.hintlabel.place(x=200,y=280,width=150,height=30)
        self.password = tk.Entry(self.frame, font = ('Ink Free',15,'bold'),show='*',justify='center')
        self.password.place(x=350,y=285,width=250,height=25)
        self.password.focus()
        self.confirmBtn = tk.Button(self.frame, text='Confirm', bg='white',font = ('Ink Free',20,'bold'), )
        self.confirmBtn.place(x=350,y=340,width=100,height=30)
        self.clearBtn = tk.Button(self.frame, text='Clear', bg='white',font = ('Ink Free',20,'bold'), command=self.clear)
        self.clearBtn.place(x=500,y=340,width=100,height=30)

        self.window.bind("<Return>",self.check)
        self.confirmBtn.bind("<ButtonRelease-1>", self.check)

    def check(self,event):
        if self.password.get() == '0':
            self.frame.destroy()
            MainMenu(self.window)
        else:
            self.password.delete(0,'end')
            tkinter.messagebox.askretrycancel(title='Error', message='the password is wrong')

    def clear(self):
        self.password.delete(0,'end')

#main operate window
class MainMenu():
    def __init__(self, window):
        self.window = window
        self.window.title('BikeShare - Operators')
        self.window.geometry('800x480+120+75')
        self.frame = tk.Frame(self.window,bg='aliceblue')
        self.frame.place(x=0,y=0,width=800,height=480)
        self.displaylist = [] #use this list to display better
        self.selectlist = []

        #hint&input part
        self.IDlabel = tk.Label(self.frame, text='Track one specific bike by its ID: ',font = ('Ink Free',20,'bold'),bg='aliceblue',anchor='w')
        self.IDlabel.place(x=30,y=30,width=430,height=30)
        self.IDbox = tk.Entry(self.frame, font = ('Comic Sans MS',15),justify='center')
        self.IDbox.place(x=460,y=30,width=80,height=30)
        self.Statuslabel = tk.Label(self.frame, text='Track ',font = ('Ink Free',20,'bold'),bg='aliceblue',anchor='w')
        self.Statuslabel.place(x=30,y=80,width=85,height=30)
        self.Statusbox = ttk.Combobox(self.frame,values=('All','normal','defective','working'),state = 'readonly',font = ('Ink Free',15,'bold'),justify='center')
        self.Statusbox.current(0)
        self.Statusbox.place(x=115,y=80,width=115,height=30)
        self.Loclabel = tk.Label(self.frame, text='bikes in location',font = ('Ink Free',20,'bold'),bg='aliceblue',anchor='w')
        self.Loclabel.place(x=240,y=80,width=200,height=30)
        self.Locbox = ttk.Combobox(self.frame,values=('All','1','2','3','4','5'),state = 'readonly',font = ('Ink Free',15,'bold'),justify='center')
        self.Locbox.current(0)
        self.Locbox.place(x=450,y=80,width=90,height=30)

        #operate button part
        self.TrackBtn = tk.Button(self.frame, text='Track!', bg='white',font = ('Ink Free',20,'bold'), command=self.track)
        self.TrackBtn.place(x=620,y=40,width=100,height=60)
        self.RepairBtn = tk.Button(self.frame, text='Repair', bg='white',font = ('Ink Free',20,'bold'), command=self.repair)
        self.RepairBtn.place(x=620,y=140,width=100,height=60)
        self.Tolabel1 = tk.Label(self.frame, text='To', bg='white',font = ('Ink Free',20,'bold'),)
        self.Tolabel1.place(x=620,y=240,width=50,height=30)
        self.Goalbox1=ttk.Combobox(self.frame,values=('1','2','3','4','5'),state = 'readonly',font = ('Ink Free',20,'bold'),justify='center')
        self.Goalbox1.place(x=670,y=240,width=50,height=30)
        self.Goalbox1.current(0)
        self.MoveBtn = tk.Button(self.frame, text='Move', bg='white',font = ('Ink Free',20,'bold'), command=self.move)
        self.MoveBtn.place(x=620,y=270,width=100,height=30)
        self.Numberbox = tk.Entry(self.frame, font = ('Ink Free',15,'bold'),justify='center')
        self.Numberbox.place(x=620,y=340,width=35,height=30)
        self.Tolabel2 = tk.Label(self.frame, text='To', bg='white',font = ('Ink Free',15,'bold'),)
        self.Tolabel2.place(x=655,y=340,width=30,height=30)
        self.Goalbox2 = ttk.Combobox(self.frame,values=('1','2','3','4','5'),state = 'readonly',font = ('Ink Free',15,'bold'),justify='center')
        self.Goalbox2.place(x=685,y=340,width=35,height=30)
        self.Goalbox2.current(0)
        self.AddBtn = tk.Button(self.frame, text='Add', bg='white',font = ('Ink Free',20,'bold'), command=self.add)
        self.AddBtn.place(x=620,y=370,width=100,height=30)

        #Tree part
        self.tree = ttk.Treeview(self.frame, show="headings", columns=(0,1,2))
        self.vbar = ttk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.vbar.set)
        self.tree.column(0, width=120, anchor="w",)
        self.tree.column(1, width=120, anchor="center")
        self.tree.column(2, width=120, anchor="center")
        self.tree.heading(0, text="ID",anchor="w",)
        self.tree.heading(1, text="Status")
        self.tree.heading(2, text="Location")
        self.tree.place(x=30,y=140,width=490,height=300)
        self.vbar.place(x=520,y=140,width=20,height=300)
        self.result = tk.Label(self.frame, bg='aliceblue',font = ('Comic Sans MS',11),anchor='w')
        self.result.place(x=30,y=440,width=150,height=20)
        self.tree.bind('<ButtonRelease-1>', self.select)
        ttk.Style().configure("Treeview.Heading", rowheight=24,font=("Comic Sans MS", 12))
        ttk.Style().configure("Treeview",rowheight=24, font=("Comic Sans MS", 12))

    def display(self,result):
        for item in result:
            self.tree.insert('','end',values=item)   

    def cleartree(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

    def checklocation(self):
        for i in range(1,6):
            cursor.execute(f'''SELECT * from bike where location_id={i}''')
            number = len(cursor.fetchall())
            if number==0:
                cursor.execute(f'''UPDATE location SET location_status = 'Empty' where location_id={i}''')
            elif number==200:
                cursor.execute(f'''UPDATE location SET location_status = 'Full' where location_id={i}''')
            else:
                cursor.execute(f'''SELECT * from bike where location_id={i} and bike_status='normal' ''')
                normal_number = len(cursor.fetchall())
                if normal_number==0:
                    cursor.execute(f'''UPDATE location SET location_status = 'No normal bikes' where location_id={i}''')
                else:
                    cursor.execute(f'''UPDATE location SET location_status = 'Available' where location_id={i}''')
        bs.commit()

    def select(self,event):#record all selected bikes' id in selectlist for repairing&moving
        self.selectlist = []
        for item in self.tree.selection():
            self.selectlist.append(int(self.tree.item(item,"values")[0]))

    def track(self):
        ID = self.IDbox.get()
        status = self.Statusbox.get()
        location = self.Locbox.get()
        invalid = 0
        if ID=='':
            if status=='All':
                if location=='All':
                    cursor.execute(f'''SELECT bikeid,bike_status,location_id from bike ''')
                else:
                    cursor.execute(f'''SELECT bikeid,bike_status,location_id from bike where location_id='{location}' ''')
            else:
                if location=='All':
                    cursor.execute(f'''SELECT bikeid,bike_status,location_id from bike where bike_status='{status}' ''')
                else:
                    cursor.execute(f'''SELECT bikeid,bike_status,location_id from bike where location_id={location} and bike_status='{status}' ''')
        else:
            try:
                ID = int(ID)
                cursor.execute(f'''SELECT bikeid,bike_status,location_id from bike where bikeid={ID} ''')
            except:
                self.IDbox.delete(0, tk.END)
                invalid = 1
                tkinter.messagebox.showwarning('warning','Invalid input!',icon= None,type= None)
        self.IDbox.delete(0, tk.END)
        resultlist = cursor.fetchall()#copy the fetch result in time for the fetchall is valid only one time
        if len(resultlist)==0 and invalid==0:
            tkinter.messagebox.showinfo('information','No matched result',icon= None,type= None)
        elif invalid==0:
            self.displaylist = resultlist
            for i in range(len(self.displaylist)):
                self.displaylist[i] = list(self.displaylist[i])
            self.cleartree()
            self.display(self.displaylist)
            self.result['text'] = f'{len(self.displaylist)}  result(s)'
        self.selectlist = []

    def repair(self):
        mark = 0
        for i in self.selectlist:
            for item in self.displaylist:
                if item[0]==i and item[1]=='defective':
                    item[1]='normal'
                    cursor.execute(f'''UPDATE bike SET bike_status = 'normal' where bikeid={i} ''')
                    cursor.execute(f'''INSERT INTO operations
                    (operation_type,bikeid,start_location,end_location,operate_time)values('repair',{i},{item[2]},{item[2]},datetime('now'))''')
                    bs.commit()
                elif item[0]==i and item[1] in ['normal','working']:
                    mark = 1
                    break
        if mark==1:
            tkinter.messagebox.showwarning('warning','Working/Normal bikes cannot be repaired',icon= None,type= None)
        self.cleartree()
        self.display(self.displaylist)
        self.selectlist=[]

    def move(self):
        samemark = 0
        workmark = 0
        end_location = int(self.Goalbox1.get())
        cursor.execute(f'''SELECT * From bike where location_id = {end_location}''')
        end_location_bikes = len(cursor.fetchall())
        if len(self.selectlist)+end_location_bikes > 200:
            tkinter.messagebox.showwarning('warning',f'{200-end_location_bikes} space in location {end_location}')
        else:
            for i in self.selectlist:
                for item in self.displaylist:
                    if item[0]==i and item[1]!='working' and item[2]!=end_location:
                        start_location=item[2]
                        item[2]=end_location
                        cursor.execute(f'''UPDATE bike SET location_id = {end_location} where bikeid={i} ''')
                        cursor.execute(f'''INSERT INTO operations
                        (operation_type,bikeid,operate_time,start_location,end_location)
                        values('move',{i},datetime('now'),{start_location},{end_location})''')
                        bs.commit()
                    elif item[0]==i and item[1]=='working':
                        workmark = 1
                        break
                    elif item[0]==i and item[2]==end_location:
                        samemark = 1
                        break
        if samemark==1:
            tkinter.messagebox.showwarning('warning','Bikes cannot be moved to its original location',icon= None,type= None)
        if workmark==1:
            tkinter.messagebox.showwarning('warning','Working bikes cannot be moved',icon= None,type= None)
        self.cleartree()
        self.display(self.displaylist)
        self.checklocation()
        self.selectlist=[]

    def add(self):
        cursor.execute(f'''SELECT count(*) from bike  ''')
        total = cursor.fetchall()[0][0]
        number = self.Numberbox.get()
        goal = int(self.Goalbox2.get())
        cursor.execute(f'''SELECT * From bike where location_id = {goal}''')
        end_location_bikes = len(cursor.fetchall())
        newlist = []#use new list in stead of self.displaylist to ensure move/repair could work if failing to add after clicking add button
        if number == '':
            tkinter.messagebox.showwarning('warning','Please enter a number',icon= None,type= None)
        else:
            try:
                number = int(number)
                if number>0 and number+end_location_bikes > 200:
                    tkinter.messagebox.showwarning('warning',f'{200-end_location_bikes} space in location {self.Goalbox2.get()}')
                elif number>0:
                    for i in range(total,total+number):
                        cursor.execute(f'''INSERT INTO bike(bikeid,location_id,bike_status)values({i},{goal},'normal')''')
                        cursor.execute(f'''INSERT INTO operations(operation_type,bikeid,operate_time,start_location,end_location)
                        values('add',{i},datetime('now'),{goal},{goal})''')
                        newlist.append([i,'normal',goal])
                        bs.commit()
                    tkinter.messagebox.showwarning('hint','Done!',icon= None,type= None)
                    self.Numberbox.delete(0, tk.END)
                    self.cleartree()
                    self.displaylist = newlist #match to move method so that the bikes could be moved after added immediately
                    self.display(newlist)
                    self.result['text'] = f'{len(self.displaylist)}  result(s)'
                    self.checklocation()
                else:
                    tkinter.messagebox.showwarning('warning','Invalid number',icon= None,type= None)
                    self.Numberbox.delete(0, tk.END)
            except:
                tkinter.messagebox.showwarning('warning','Invalid input!',icon= None,type= None)
                self.Numberbox.delete(0, tk.END)
          
#main
if __name__ == '__main__': 
    window = tk.Tk()
    window.resizable(0,0)
    Confirm(window)
    window.mainloop()
    
bs.close()
