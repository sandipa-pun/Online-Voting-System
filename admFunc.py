import tkinter as tk
import dframe as df
from tkinter import *
from dframe import *
from PIL import ImageTk, Image
from tkinter import ttk
from dframe import encrypt, decrypt

def resetAll(root, frame1):
    Label(frame1, text="").grid(row=10, column=0)
    msg = Message(frame1, text="Reset Complete", width=500)
    msg.grid(row=11, column=0, columnspan=5)

def showVotes(root, frame1):
    result = df.show_result()
    root.title("Votes")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Vote Count", font=('Helvetica', 20, 'bold')).grid(row=0, column=1, columnspan=3)
    Label(frame1, text="").grid(row=1, column=0)

    Label(frame1, text="Youth                   ", font=('Helvetica', 15, 'bold')).grid(row=2, column=1, sticky='e')
    Label(frame1, text=result['youth'], font=('Helvetica', 15, 'bold')).grid(row=2, column=2, sticky='w')

    Label(frame1, text="IT                  ", font=('Helvetica', 15, 'bold')).grid(row=3, column=1, sticky='e')
    Label(frame1, text=result['it'], font=('Helvetica', 15, 'bold')).grid(row=3, column=2, sticky='w')

    Label(frame1, text="Sports                  ", font=('Helvetica', 15, 'bold')).grid(row=4, column=1, sticky='e')
    Label(frame1, text=result['sports'], font=('Helvetica', 15, 'bold')).grid(row=4, column=2, sticky='w')

    Label(frame1, text="Event                   ", font=('Helvetica', 15, 'bold')).grid(row=5, column=1, sticky='e')
    Label(frame1, text=result['event'], font=('Helvetica', 15, 'bold')).grid(row=5, column=2, sticky='w')

    Label(frame1, text="News                    ", font=('Helvetica', 15, 'bold')).grid(row=6, column=1, sticky='e')
    Label(frame1, text=result['news'], font=('Helvetica', 15, 'bold')).grid(row=6, column=2, sticky='w')
    

def details(root, frame1):
    result = df.voterdetails()
    root.title("Voter Details")
    for widget in frame1.winfo_children():
        widget.destroy()
        
    heading_label = Label(frame1, text="Voter Details", font=("Helvetica", 18, "bold"))
    heading_label.pack(side="top", pady=10)

    tree = ttk.Treeview(frame1, columns=("voter_id", "stdid", "name", "batch", "faculty","password", "hasVoted"), show="headings", height=5)  
    tree.heading("voter_id", text="Voter ID") 
    tree.heading("stdid", text="Student ID") 
    tree.heading("name", text="Name") 
    tree.heading("batch", text="Batch") 
    tree.heading("faculty", text="Faculty") 
    tree.heading("password", text="password")
    tree.heading("hasVoted", text="Has Voted") 


    for col in ("voter_id", "stdid", "name", "batch", "faculty", "password","hasVoted"):
        tree.column(col, anchor="center")

    for voter in result:
        tree.insert("", "end", values=(voter['Voter ID'], voter['Student ID'], voter['Name'], voter['Batch'], voter['Faculty'], voter['password'], voter['Has Voted']))

    tree.pack(expand=True, fill="both", padx=10, pady=10)

    frame1.pack()
    root.mainloop()







