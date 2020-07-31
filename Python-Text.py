from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import *
import tkinter as tk
import os
import sys

filename = None

#ALL FUNCTIONS

def newFile():
    global filename
    filename = "Untitled"
    f = asksaveasfile(mode='x')
    text.delete(0.0, END)
        
def saveFile():
    global filename
    t = text.get(0.0, END)
    f = open(filename, 'Untitled')
    f.write(t)
    f.close()
                          
def saveAs():
    f = asksaveasfile(mode='w')                   
    t = text.get(0.0, END)
    try:
        f.write(t.strip())
    except:
        showerror(title="Error!", message="not is possible save")
            
def openFile():
    f = askopenfile(mode='r')
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)

#ROOT TO MAKE A MENU BAR  

root = Tk()
root.title("Python-Text")
root.minsize(width=400, height=400)
root.maxsize(width=400, height=400)

#TEXT SETTINGS

text = Text(root, width=400, height=400)
text.pack()

#MENUBAR FUNCTIONS IN PROGRAM

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar)
filemenu.add_command(label="New File",  command=newFile)
filemenu.add_command(label="Open",  command=openFile)
filemenu.add_command(label="Save",  command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Exit",  command=root.quit)

menubar.add_cascade(label="Options", menu=filemenu)

root.config(menu=menubar)
root.mainloop()
