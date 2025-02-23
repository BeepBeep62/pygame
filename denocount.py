import tkinter as tk
from tkinter import messagebox
from tkinter import *
Window = Tk()
Window.title("tk")
Window.geometry("410x390")#
Window.configure(bg='Cyan')
label1 = Label(Window, text="hello user, welcome to gambling simulator")
label1.place(relx=0.2,y=150)
def Topwin():
    Top = Toplevel()
    Top.title("Gambling Simulator")
    Top.geometry('400x380')
    Top.configure(bg='blue')
    l1 = Label(Top,text='enter ur all personal information (total amount)', bg='red')
    entre = Entry(Top)
    l2 = Label(Top, text=('heres ur'))
    l3 = Label(Top, text='2000')
    l4 = Label(Top, text='500')
    l5= Label(Top, text='100')
    t1 = Entry(Top)
    t2 = Entry(Top)
    t3 = Entry(Top)
    def calculator():
        try:
            global amount
            amount = int(entre.get())
            notes_of_2000 = amount//2000
            amount=amount%2000
            notes_of_500 = amount//500
            amount=amount%500
            notes_of_100 = amount//100
            amount=amount%100
            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)
            t1.insert(END,str(notes_of_2000))
            t2.insert(END,str(notes_of_500))
            t3.insert(END,str(notes_of_100))
        except ValueError:
            messagebox.showerror(
                'error','ples enter valid number'
            )
    buttun = Button(Top, text='calculate', command=calculator)
    l1.place(x=100,y=50)
    entre.place(x=150,y=80)
    buttun.place(x=150,y=120)
    l2.place(x=150,y=150)
    l3.place(x=150,y=200)
    t1.place(x=200,y=200)
    l4.place(x=150,y=230)
    t2.place(x=200,y=230)
    l5.place(x=150,y=250)
    t3.place(x=200,y=250)
    Top.mainloop()
def msgbox():
    box = messagebox.showinfo('Alert!', 'you have been skibidi rizzlerd, ur luck was so bad that y0ou lost all your money to this gambling simulator')
    if box=='ok':
        Topwin()
buttongetstartet = Button(Window, text="Get Started",command=msgbox)
buttongetstartet.place(x=300,y=300)
Window.mainloop()