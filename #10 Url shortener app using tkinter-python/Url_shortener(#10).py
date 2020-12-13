from tkinter import *
import tkinter.ttk as ttk
from ttkthemes import ThemedTk
from tkinter import messagebox
import pyshorteners
import webbrowser

def logic():
    s = pyshorteners.Shortener()
    a = s.tinyurl.short('www.google.com')
    messagebox.showinfo("This is your URL",a)
    

def callback():
    url = "www.google.com"
    webbrowser.open_new(url)

tk = ThemedTk(theme = 'clam')
tk.title("Url shortener")
tk.geometry("500x500")
fname = PhotoImage(file = 'image1.png')
background_label = Label(tk, image = fname)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

b1 = ttk.Button(tk, text="Click to open the link", command = callback).pack()
b2 = ttk.Button(tk, text="Click to shorten the URL", command = logic).pack()

tk.mainloop()
