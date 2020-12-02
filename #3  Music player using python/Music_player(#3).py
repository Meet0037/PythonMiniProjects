#import all modules which is required
from tkinter import *
from ttkthemes import ThemedTk
import tkinter.ttk as ttk
from pygame import mixer

mixer.init()
mixer.music.load('song1.wav')

#define function
def playsong():
    mixer.music.play()
def stopsong():
    mixer.music.stop()
def pausesong():
    mixer.music.pause()
def resumesong():
    mixer.music.unpause()

window = ThemedTk(theme="equilux")
window.geometry('300x300')
window.configure(bg = 'yellow')
window.title('Music Player')
playbutton = ttk.Button(window, text='Play', command = playsong).grid(column=0, row=1)
stopbutton = ttk.Button(window, text='Stop', command = stopsong).grid(column=1, row=1)
pausebutton = ttk.Button(window, text='Pause', command = pausesong).grid(column=2, row=1)
resumebutton = ttk.Button(window, text='Resume', command = resumesong).grid(column=1, row=2)

window.mainloop()

