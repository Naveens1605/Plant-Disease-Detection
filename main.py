from tkinter import Tk
from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import tkinter as tk



def gentk():
    root.withdraw()
    import cnn

def run():
    root.destroy()
    import ui

root = Tk()
root.geometry("500x500")


topframe = Frame(root)
topframe.pack()
bottomframe = Frame(root)
bottomframe.pack()

w=Label(topframe,text="PLANT DISEASE DETECTION")
w.config(font=('time',20))
w.pack()

btn1=Button(bottomframe,text="Train Data",command=gentk)
btn1.grid(column=0)
btn = Button(bottomframe,text="Start the Detection",command=run)
btn.grid(column=0)
root.mainloop()