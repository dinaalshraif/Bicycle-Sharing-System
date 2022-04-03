import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import sqlite3
import matplotlib
matplotlib.use("Qt5Agg")
import matplotlib.pyplot as plt
import numpy as np

bs = sqlite3.connect('bikeshare.db')
cursor = bs.cursor()

#confirm window to check password
class Confirm():
    def __init__(self, window):
        self.window = window
        self.window.title('BikeShare - Manager:Login')
        self.window.geometry('800x480+120+75')
        self.frame = tk.Frame(self.window,bg='Lavender')
        self.frame.place(x=0,y=0,width=800,height=480)
        
        self.hintlabel = tk.Label(self.frame, text='Dear Manager, Welcome! ',font = ('Ink Free',30,'bold'),bg='Lavender',anchor='w')
        self.hintlabel.place(x=200,y=120,width=450,height=60)
        self.hintlabel = tk.Label(self.frame, text='Password: ',font = ('Ink Free',20,'bold'),bg='Lavender',anchor='w')
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
        if self.password.get() == '1':
             self.frame.destroy()
             ManagerMenu(self.window)
        else:
            self.password.delete(0,'end')
            tkinter.messagebox.askretrycancel(title='Error', message='the password is wrong')

    def clear(self):
        self.password.delete(0,'end')
                
#main operate window
class ManagerMenu():
    def __init__(self, window):
        self.window = window
        self.window.title('BikeShare - Manager')
        self.window.geometry('800x480+120+75')
        self.frame = tk.Frame(self.window,bg='Lavender')
        self.frame.place(x=0,y=0,width=800,height=480)
        self.displaylist = [] #use this list to display better
        self.start_dict = {}
        self.end_dict = {}

        #hint&input part
        self.timeLabel = tk.Label(self.frame, text='Generate reports showing all bike activities',font = ('Ink Free',20,'bold'),bg='Lavender',anchor='w')
        self.timeLabel.place(x=30,y=30,width=600,height=30)
        self.start_time = tk.Label(self.frame,text='Start time',font = ('Ink Free',20,'bold'),bg='Lavender',anchor='w')
        self.start_time.place(x=30,y=60,width=200,height=30)
        self.end_time = tk.Label(self.frame,text='End time',font = ('Ink Free',20,'bold'),bg='Lavender',anchor='w')
        self.end_time.place(x=300,y=60,width=200,height=30)
        self.start_time_box = tk.Entry(self.frame, font = ('Comic Sans MS',15),justify='center')
        self.start_time_box.place(x=30,y=90,width=250,height=30)
        self.end_time_box = tk.Entry(self.frame, font = ('Comic Sans MS',15),justify='center')
        self.end_time_box.place(x=300,y=90,width=250,height=30)
        self.tips = tk.Label(self.frame, text='(input like 2021-02-12 09:00:00)',font = ('Ink Free',20,'bold'),bg='Lavender',anchor='w')
        self.tips.place(x=30,y=120,width=500,height=30)
        
        #Manager button part
        self.report = tk.Button(self.frame,text='Report', bg='white',font = ('Ink Free',20,'bold'), command=self.show_data)
        self.report.place(x=570,y=90,width=100,height=50)
        self.clear = tk.Button(self.frame,text='Clear', bg='white',font = ('Ink Free',20,'bold'), command=self.clear)
        self.clear.place(x=690,y=30,width=100,height=50)
        self.chart = tk.Button(self.frame,text='Chart', bg='white',font = ('Ink Free',20,'bold'), command=self.chart)
        self.chart.place(x=690,y=90,width=100,height=50)
        
        #Tree part
        self.tree = ttk.Treeview(self.frame, show="headings", columns=(0,1,2,3,4,5,6))
        self.vbar = ttk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.vbar.set)
        self.tree.column(0, width=50, anchor="w")
        self.tree.column(1, width=100, anchor="center")
        self.tree.column(2, width=170, anchor="center")
        self.tree.column(3, width=170, anchor="center")
        self.tree.column(4, width=85, anchor="center")
        self.tree.column(5, width=85, anchor="center")
        self.tree.column(6, width=110, anchor="center")
        self.tree.heading(0, text="Bike Id",anchor="w")
        self.tree.heading(1, text="User Id",anchor="w")
        self.tree.heading(2, text="Start Time")
        self.tree.heading(3, text="End Time")
        self.tree.heading(4, text="Start Location")
        self.tree.heading(5, text="End Location")
        self.tree.heading(6, text="Activity Type")
        self.tree.place(x=10,y=150,width=760,height=300)
        self.vbar.place(x=770,y=150,width=20,height=300)
        self.tree.bind('<ButtonRelease-1>', self.select)
        
    def select(self,event):#record all selected bikes' id in selectlist for repairing&moving
        self.selectlist = []
        for item in self.tree.selection():
            self.selectlist.append(int(self.tree.item(item,"values")[0]))

    def show_data(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.displaylist = []
        datalist=[]
        self.displaylist = datalist
        info = cursor.execute('''SELECT bikeid,userid,start_time,end_time,start_location,end_location from ride where start_time>=?AND end_time<=?''',(self.start_time_box.get(),self.end_time_box.get()) ).fetchall()
        tuple_ride=("ride",)
        for i in info:
            datalist.append(i+tuple_ride)          
        info_oper = cursor.execute('''SELECT bikeid,operationid,operate_time,operate_time,start_location,end_location,operation_type from operations where operate_time>=?AND operate_time<=?''',(self.start_time_box.get(),self.end_time_box.get())).fetchall()
        for i in info_oper:
            datalist.append(i)
        if len(info) | len(info_oper) :
            self.display(datalist)
            datalist=[]
        else:
            tkinter.messagebox.showinfo("no activity in this time period", 'No matched result')
            
    def display(self,result):
        for item in result:
            self.tree.insert('','end',values=item)   

    def clear(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
            
    def chart(self):
        start_dict = {(1,): 0, (2,): 0, (3,): 0, (4,): 0, (5,): 0}
        end_dict = {(1,): 0, (2,): 0, (3,): 0, (4,): 0, (5,): 0}
        info = cursor.execute('''SELECT start_location from ride where start_time>=?AND end_time<=?''',
                              (self.start_time_box.get(), self.end_time_box.get())).fetchall()
        for i in info:
            start_dict[i] = start_dict.get(i) + 1     
        info = cursor.execute('''SELECT end_location from ride where start_time>=?AND end_time<=?''',
                              (self.start_time_box.get(), self.end_time_box.get())).fetchall()
        for i in info:
            end_dict[i] = end_dict.get(i) + 1
        self.start_dict = start_dict
        self.end_dict = end_dict
        index = np.arange(5)
        bw=0.3
        start_list=list(self.start_dict.values())
        end_list=list(self.end_dict.values())
        y_max=max(max(start_list),max(end_list))
        plt.figure(figsize=(6,4))
        plt.axis([0,5,0,y_max])
        plt.title('The number of bike in start and end location')
        plt.bar(index,start_list,bw,color='b',label='Start')
        plt.bar(index+bw,end_list,bw,color='r',label='End')
        plt.xticks(index+0.5*bw,['1','2','3','4','5'])
        plt.legend()
        
#main
if __name__ == '__main__': 
    window = tk.Tk()
    window.resizable(0,0)
    Confirm(window)
    window.mainloop()
    
bs.close()

