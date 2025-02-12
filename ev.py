import tkinter
from tkinter import *
window = Tk()
window.title("n word")
window.geometry("300x300")
def die(event):
    print("key_pressed =", event.char)
window.bind('<Key>', die)
def buttonhandler(event):
    print("button_clicked")
button = Button(text="button", bg="blue",fg="white")
button.pack()
button.bind('<Button-1>', buttonhandler)
window.mainloop()