from tkinter import *
from tkinter import messagebox
import pyspeedtest

def test():
    st = pyspeedtest.SpeedTest("www.google.com")
    a = (str(st.download()) + "[Bytes per second]")
    messagebox.showinfo("Your download speed : ",a)

tk = Tk()
tk.title("Meet speed Test")
tk.geometry('500x500')
fname = PhotoImage(file="speed.png")
background_label = Label(tk, image = fname)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

b = Button(tk, text="Click to check internet speed", font=('San serif',20), bg="Orange", height=1, width=30, command=test).pack()
tk.mainloop()
