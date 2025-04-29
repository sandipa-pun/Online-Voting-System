import subprocess as sb_p
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from Admin import AdmLogin
from voter import voterLogin

def Home(root, frame1, frame2):
    for frame in root.winfo_children():
        for widget in frame.winfo_children():
            widget.destroy()
            
    def go_home():
        Home(root, frame1, frame2)

    def open_admin_login():
        AdmLogin(root, frame1)

    def open_voter_login():
        voterLogin(root, frame1)

    menubar = Menu(root)
    root.config(menu=menubar)

    menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Menu", menu=menu)

    menu.add_command(label="Home", command=go_home)
    menu.add_separator()
    menu.add_command(label="Exit", command=quit)

    login = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Login", menu=login)

    login.add_command(label="Admin Login", command=open_admin_login)
    login.add_command(label="Voter Login", command=open_voter_login)

    frame2.pack(side=TOP)

    root.title("Home")

    Label(frame1, text="Welcome to Online Voting System!", font=('Helvetica', 17, 'bold'), fg="#001C30").grid(row=0, column=0, padx=10, pady=10)
    Label(frame1, text="Vote for the best Candidate", font=('Helvetica', 15, 'bold'), fg="#001C30").grid(row=1, column=0, padx=10, pady=10)

    logo_image = Image.open("Softwarica-logo.png")
    logo_image = logo_image.resize((500, 100)) 
    logo_photo = ImageTk.PhotoImage(logo_image)
    logo_label = Label(frame2, image=logo_photo)
    logo_label.pack(side=TOP)

    frame1.pack(expand=True, padx=50, pady=50)
    root.mainloop()


def new_home():
    root = Tk()
    root.geometry('1000x600')
    root.configure(bg="#EEEDED")  
    frame1 = Frame(root)
    frame2 = Frame(root)
    frame2.pack()
    Home(root, frame1, frame2)

if __name__ == "__main__":
    new_home()





