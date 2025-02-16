from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
Window = Tk()
Window.title("tk")
Window.geometry("410x390")
Window.rowconfigure(0, minsize=800, weight=1)
Window.columnconfigure(1, minsize=800, weight=1)
textedit = Text(Window)
fb = Frame(Window, relief=RAISED)
def importfile():
    filepath = askopenfilename(filetypes=[('text files', '*.txt'),('All Files','*.*')])
    if not filepath:
        return
    textedit.delete(1.0,END)
    with open(filepath,'r') as textinput:
        text = textinput.read()
        textedit.insert(END, text)
        textinput.close()
def exportfile():
    filepath=asksaveasfilename(defaultextension='txt', filetypes=[('text files', '*.txt'),('All Files','*.*')])
    if not filepath:
        return
    with open(filepath,'w') as outputfile:
        text=textedit.get(1.0,END)
        outputfile.write(text)
buttonimport = Button(fb, text="import",command=importfile)
buttonexport = Button(fb, text="export", command=exportfile)
buttonimport.grid(row=0,column=0,padx=5,pady=5)
buttonexport.grid(row=1,column=0,padx=5,pady=5)
fb.grid(row=0,column=0, sticky="ns")
textedit.grid(row=0,column=1,sticky='nsew')
Window.mainloop()