import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os



#function for play button
def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()

#function for stop button
def stop():
    pygame.mixer.music.stop()

#function for pause button
def pause():
    pygame.mixer.music.pause()

#function for resume button
def resume():
    pygame.mixer.music.unpause()
    

#Creting window
musicplayer = tkr.Tk()

#setting the title Name
musicplayer.title("Music player")

#setting the window dimention
musicplayer.geometry("450x350")

#Asking for user directory
directory = askdirectory()

#Setting music directory to the current working directory
os.chdir(directory)

#Creating our songList
songlist = os.listdir()

#Creating the playlist
playlist = tkr.Listbox(musicplayer, font = "Arial 15 bold", bg = "cyan2", selectmode = tkr.SINGLE)

#Adding song from songlist to playlist
for item in songlist:
    pos = 0
    playlist.insert(pos, item)
    pos = pos + 1

#Initialising modules
pygame.init()
pygame.mixer.init()

var = tkr.StringVar()
songtitle = tkr.Label(musicplayer, font = "Arial 15 bold", textvariable = var)
songtitle.pack()


#creating buttons
Button_play = tkr.Button(musicplayer, height=3, width=5, text="Play music", font = "Arial 15 bold", command = play, bg = "orange", fg = "white")
Button_stop = tkr.Button(musicplayer, height=3, width=5, text="Stop music", font = "Arial 15 bold", command = stop, bg = "yellow", fg = "purple")
Button_pause = tkr.Button(musicplayer, height=3, width=5, text="Pause music", font = "Arial 15 bold", command = pause, bg = "red", fg = "white")
Button_resume = tkr.Button(musicplayer, height=3, width=5, text="resume music", font = "Arial 15 bold", command = resume, bg = "green", fg = "orange")

Button_play.pack(fill = "x")
Button_stop.pack(fill = "x")
Button_pause.pack(fill = "x")
Button_resume.pack(fill = "x")

playlist.pack(fill="both", expand="yes")


musicplayer.mainloop()
