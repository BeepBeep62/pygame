# Create a Tkinter Application which consists of a root window with a button (with text Scan for the virus). When this button is clicked, it will generate a message box that shows a warning: Stop! Virus Found.
import tkinter
from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("au revoir")
window.geometry("200x200")
def message():
    messagebox.showwarning("ALERT","YOUR PC HAS BEEN HACKED AND NOW UR IN DEBT OF 160 VIRGINTILLION DOLLARS")
button = Button(window, text="free robux", bg="green",fg="red", command=message)
button.place(x=100,y=100)
window.mainloop()