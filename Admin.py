
import subprocess as sb_p
import tkinter as tk
import registerVoter as regV
import admFunc as adFunc
import dframe as df
from tkinter import *
from registerVoter import *
from admFunc import *
from dframe import *

def AdminHome(root, frame1, frame3):
    root.title("Admin")
    for widget in frame1.winfo_children():
        widget.destroy()

    frame1.config(width=2000, height=1000)  

    Label(frame1, text="Admin", font=('Helvetica', 20, 'bold'), fg="#001C30", justify='center').grid(row=0, column=1, columnspan=3)
    Label(frame1, text="").grid(row=1, column=0)

    runServer = Button(frame1, text="Run Server", height=3, width=90, command=lambda: sb_p.call('start python Server.py', shell=True))
    registerVoter = Button(frame1, text="Register Voter", height=3, width=90, command=lambda: regV.Register(root, frame1))
    showVotes = Button(frame1, text="Show Votes",height=3, width=90, command=lambda: adFunc.showVotes(root, frame1))
    details = Button(frame1, text="Show Voter Details", height=3,width=90, command=lambda: adFunc.details(root, frame1))
    

    Label(frame1, text="").grid(row=2, column=0)
    Label(frame1, text="").grid(row=4, column=0)
    Label(frame1, text="").grid(row=6, column=0)
    Label(frame1, text="").grid(row=8, column=0)
    runServer.grid(row=3, column=1, columnspan=2)
    registerVoter.grid(row=5, column=1, columnspan=2)
    showVotes.grid(row=7, column=1, columnspan=2)
    details.grid(row=9, column=1, columnspan=2)

    frame1.pack()
    root.mainloop()


def log_admin(root,frame1,admin_ID,password):

    if(admin_ID=="Admin" and password=="admin"):
        frame3 = root.winfo_children()[1]
        AdminHome(root, frame1, frame3)
    else:
        msg = Message(frame1, text="Either ID or Password is Incorrect", width=500, fg="red")
        msg.grid(row = 6, column = 0, columnspan = 5)


def AdmLogin(root, frame1):
    root.title("Admin Login")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Admin Login", font=('Helvetica', 20, 'bold'), fg="#001C30").grid(row=0, column=2, rowspan=1)
    Label(frame1, text="").grid(row=1, column=0)
    Label(frame1, text="Admin ID:      ", anchor="e", justify=LEFT).grid(row=2, column=0)
    Label(frame1, text="Password:       ", anchor="e", justify=LEFT).grid(row=3, column=0)

    admin_ID = tk.StringVar()
    password = tk.StringVar()

    e1 = Entry(frame1, textvariable=admin_ID)
    e1.grid(row=2, column=2, columnspan=3)  
    e2 = Entry(frame1, textvariable=password, show='*')
    e2.grid(row=3, column=2, columnspan=3)  

    sub = Button(frame1, text="Login", width=10, command=lambda: log_admin(root, frame1, admin_ID.get(), password.get()))
    Label(frame1, text="").grid(row=4, column=0)
    sub.grid(row=5, column=3, columnspan=2)

    frame1.pack()
    root.mainloop()