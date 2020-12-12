from tkinter import *
import wikipedia

def on_click():
    q = get_q.get()
    text.insert(INSERT, wikipedia.summary(q))

def change_color():
    current_color = tk.cget("background")
    next_color = "lightgreen" if current_color == "red" else "red"
    tk.config(background=next_color)
    tk.after(1000, change_color)

tk = Tk()

tk.title("Wikipedia App")
que = Label(tk, text='Question')
que.pack()
Text(tk, background="lightgreen")
change_color()

get_q = Entry(tk, bd=5)
get_q.pack()
submit = Button(tk, text='Search', command=on_click)
submit.pack()

text = Text(tk)

text.pack()

tk.mainloop()
