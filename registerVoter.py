import tkinter as tk
import dframe as df
import Admin as adm
from tkinter import ttk
from Admin import *
from tkinter import *
from dframe import *

def reg_server(root,frame1,stdid,name,batch,faculty,password,conpass):
    if(password=='' or password==' '):
        msg = Message(frame1, text="Error: Missing Fileds", width=500, fg="red")
        msg.grid(row = 10, column = 0, columnspan = 5)
        return -1
    
    if(stdid=='' or stdid==' '):
        msg = Message(frame1, text="Error: Missing Fileds", width=500, fg="red")
        msg.grid(row = 10, column = 0, columnspan = 5)
        return -1

    if(password!=conpass):
        msg = Message(frame1, text="Error: Passwords Donot Match", width=500, fg="red")
        msg.grid(row = 10, column = 0, columnspan = 5)
        return -1
    
    vid = df.taking_data_voter(stdid, name, batch, faculty, password, conpass)
    for widget in frame1.winfo_children():
        widget.destroy()
    txt = "Registered Voter with\n\n VOTER I.D. = " + str(vid)
    Label(frame1, text=txt, font=('Helvetica', 18, 'bold')).grid(row = 2, column = 1, columnspan=2)


def Register(root,frame1):

    root.title("Register Voter")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Register Voter", font=('Helvetica', 18, 'bold')).grid(row = 0, column = 2, rowspan=1)
    Label(frame1, text="").grid(row = 1,column = 0)
    Label(frame1, text="Student ID:         ", anchor="e", justify=LEFT).grid(row = 3,column = 0)
    Label(frame1, text="Name:              ", anchor="e", justify=LEFT).grid(row = 4,column = 0)
    Label(frame1, text="Batch:           ", anchor="e", justify=LEFT).grid(row = 5,column = 0)
    Label(frame1, text="Faculty:           ", anchor="e", justify=LEFT).grid(row = 6,column = 0)
    Label(frame1, text="Password:             ", anchor="e", justify=LEFT).grid(row = 7,column = 0)
    Label(frame1, text="Con Password:   ", anchor="e", justify=LEFT).grid(row = 8 ,column = 0)


    stdid = tk.StringVar()
    name = tk.StringVar()
    batch = tk.StringVar()
    faculty = tk.StringVar()
    password= tk.StringVar()
    conpass = tk.StringVar()

    e2 = Entry(frame1, textvariable = stdid).grid(row = 3, column = 2)
    e3 = Entry(frame1, textvariable = name).grid(row = 4, column = 2)
    e5 = Entry(frame1, textvariable = password,show = "*").grid(row = 7, column = 2)
    e5 = Entry(frame1, textvariable = conpass, show = "*").grid(row = 8, column = 2)
    
    e4 = ttk.Combobox(frame1, textvariable = batch, width=17)
    e4['values'] = ("29","30","31","32","33","34")
    e4.grid(row = 5, column = 2)
    e4.current()
    
    e5 = ttk.Combobox(frame1, textvariable = faculty, width=17)
    e5['values'] = ("Computing","Ethical Hacking and Cybersecurity")
    e5.grid(row = 6, column = 2)
    e5.current()


    reg = Button(frame1, text="Register", command = lambda: reg_server(root, frame1, stdid.get(), name.get(), batch.get(),faculty.get(), password.get(), conpass.get()), width=10)
    
    reg.grid(row=9, column=3, columnspan=2)

    reg.grid(row = 9, column = 3, columnspan = 2)

    frame1.pack()
    root.mainloop()


