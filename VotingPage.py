import tkinter as tk
import socket
from tkinter import *
from PIL import ImageTk,Image

def voteCast(root,frame1,vote,client_socket):

    for widget in frame1.winfo_children():
        widget.destroy()

    client_socket.send(vote.encode()) 

    message = client_socket.recv(1024) 
    print(message.decode()) 
    message = message.decode()
    if(message=="Successful"):
        Label(frame1, text="Vote Casted Successfully", font=('Helvetica', 18, 'bold')).grid(row = 1, column = 1)
        
    elif message == "WrongPassword":  
        Label(frame1, text="Wrong Password Entered\nPlease try again", font=('Helvetica', 18, 'bold'), fg="red").grid(
            row=1, column=1)
        
    else:
        Label(frame1, text="Wrong Password or Vote Already Casted\n Vote Not Valid", font=('Helvetica', 18, 'bold'), fg="red").grid(row = 1, column = 1)

    client_socket.close()



def votingPg(root,frame1,client_socket):

    root.title("Cast Vote")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Cast Vote", font=('Helvetica', 18, 'bold')).grid(row = 0, column = 1, rowspan=1)
    Label(frame1, text="").grid(row = 1,column = 0)

    vote = StringVar(frame1,"-1")

    Radiobutton(frame1, text = "Youth Club", variable = vote, value = "youth", indicator = 0, height = 3, width=90, command = lambda: voteCast(root,frame1,"youth",client_socket)).grid(row = 2,column = 1)
    Radiobutton(frame1, text = "IT Club", variable = vote, value = "it", indicator = 0, height = 3, width=90, command = lambda: voteCast(root,frame1,"it",client_socket)).grid(row = 3,column = 1)
    Radiobutton(frame1, text = "Sports Club", variable = vote, value = "sports", indicator = 0, height = 3, width=90, command = lambda: voteCast(root,frame1,"sports",client_socket) ).grid(row = 4,column = 1)
    Radiobutton(frame1, text = "Event Club", variable = vote, value = "event", indicator = 0, height = 3, width=90, command = lambda: voteCast(root,frame1,"event",client_socket)).grid(row = 5,column = 1)
    Radiobutton(frame1, text = "News Club", variable = vote, value = "news", indicator = 0, height = 3, width=90, command = lambda: voteCast(root,frame1,"news",client_socket)).grid(row = 6,column = 1)

    frame1.pack()
    root.mainloop()

if __name__ == "__main__":
    root = Tk()
    root.geometry('500x500')
    frame1 = Frame(root)
    client_socket = 'Fail'
